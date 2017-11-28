from django.db import models
from django.db import transaction
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _


class AgentManager(models.Manager):
    def create_with_details(self, user, **kwargs):
        with transaction.atomic():
            user = auth_models.User.objects.create(**user)
            agent = self.create(user=user, **kwargs)
            return agent


class Agent(models.Model):
    STAFF = "STAFF"
    AGENT = "AGENT"
    ADMIN = "ADMIN"
    USER_ROLES = (
        (STAFF, _("Staff")),
        (AGENT, _("Agent")),
        (ADMIN, _("Admin"))
    )

    user = models.OneToOneField(
        auth_models.User, on_delete=models.CASCADE, verbose_name=_("User"))
    role = models.CharField(
        verbose_name=_("Role"), max_length=255, choices=USER_ROLES, null=False,
        blank=False)
    parent = models.ForeignKey("self", null=True, verbose_name=_("Parent"))

    objects = AgentManager()

    def __str__(self):
        return "{}".format(self.user.username)
