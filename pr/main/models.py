from django.db import models
from django.utils.translation import ugettext_lazy as _

class AgentManager(models.Manager):
    pass


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
        "jango.contrib.auth.User", on_delete=models.CASCADE,
        verbose_name=_("User"))
    role = models.CharField(
        verbose_name=_("Role"), max_length=255, choices=USER_ROLES, null=False,
        blank=False)
    parent = models.ForeignKey("self", null=True, verbose_name=_("Parent"))

    objects = AgentManager()

    def __str__(self):
        return "{}".format(self.user.username)
