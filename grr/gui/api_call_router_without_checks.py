#!/usr/bin/env python
"""Implementation of a router class that does no ACL checks."""



from grr.gui import api_call_router

from grr.gui.api_plugins import aff4 as api_aff4
from grr.gui.api_plugins import artifact as api_artifact
from grr.gui.api_plugins import client as api_client
from grr.gui.api_plugins import config as api_config
from grr.gui.api_plugins import cron as api_cron
from grr.gui.api_plugins import docs as api_docs
from grr.gui.api_plugins import flow as api_flow
from grr.gui.api_plugins import hunt as api_hunt
from grr.gui.api_plugins import output_plugin as api_output_plugin
from grr.gui.api_plugins import reflection as api_reflection
from grr.gui.api_plugins import stats as api_stats
from grr.gui.api_plugins import user as api_user
from grr.gui.api_plugins import vfs as api_vfs


class ApiCallRouterWithoutChecks(api_call_router.ApiCallRouter):
  """Router that does no ACL checks whatsoever."""

  # AFF4 access methods.
  # ===================
  #
  # NOTE: These are likely to be deprecated soon in favor
  # of more narrow-scoped VFS access methods.
  def GetAff4Object(self, args, token=None):
    return api_aff4.ApiGetAff4ObjectHandler()

  def GetAff4Index(self, args, token=None):
    return api_aff4.ApiGetAff4IndexHandler()

  # Artifacts methods.
  # =================
  #
  def ListArtifacts(self, args, token=None):
    return api_artifact.ApiListArtifactsHandler()

  def UploadArtifact(self, args, token=None):
    return api_artifact.ApiUploadArtifactHandler()

  def DeleteArtifacts(self, args, token=None):
    return api_artifact.ApiDeleteArtifactsHandler()

  # Clients methods.
  # ===============
  #
  def SearchClients(self, args, token=None):
    return api_client.ApiSearchClientsHandler()

  def GetClient(self, args, token=None):
    return api_client.ApiGetClientHandler()

  # Virtual file system methods.
  # ============================
  #

  def GetFileDetails(self, args, token=None):
    return api_vfs.ApiGetFileDetailsHandler()

  def GetFileList(self, args, token=None):
    return api_vfs.ApiGetFileListHandler()

  def GetFileText(self, args, token=None):
    return api_vfs.ApiGetFileTextHandler()

  def GetFileBlob(self, args, token=None):
    return api_vfs.ApiGetFileBlobHandler()

  def GetFileVersionTimes(self, args, token=None):
    return api_vfs.ApiGetFileVersionTimesHandler()

  def GetFileDownloadCommand(self, args, token=None):
    return api_vfs.ApiGetFileDownloadCommandHandler()

  def CreateVfsRefreshOperation(self, args, token=None):
    return api_vfs.ApiCreateVfsRefreshOperationHandler()

  def GetVfsRefreshOperationState(self, args, token=None):
    return api_vfs.GetVfsRefreshOperationStateHandler()

  # Clients labels methods.
  # ======================
  #
  def ListClientsLabels(self, args, token=None):
    return api_client.ApiListClientsLabelsHandler()

  def AddClientsLabels(self, args, token=None):
    return api_client.ApiAddClientsLabelsHandler()

  def RemoveClientsLabels(self, args, token=None):
    return api_client.ApiRemoveClientsLabelsHandler()

  # Clients flows methods.
  # =====================
  #
  # Note: should be renamed to ListFlows. We should assume by default that
  # flows are client-specific. Global flows should be explicitly called
  # "global".
  def ListClientFlows(self, args, token=None):
    return api_flow.ApiListClientFlowsHandler()

  def GetFlow(self, args, token=None):
    return api_flow.ApiGetFlowHandler()

  def CreateFlow(self, args, token=None):
    return api_flow.ApiCreateFlowHandler()

  def CancelFlow(self, args, token=None):
    return api_flow.ApiCancelFlowHandler()

  def ListFlowResults(self, args, token=None):
    return api_flow.ApiListFlowResultsHandler()

  def GetFlowResultsExportCommand(self, args, token=None):
    return api_flow.ApiGetFlowResultsExportCommandHandler()

  def GetFlowFilesArchive(self, args, token=None):
    return api_flow.ApiGetFlowFilesArchiveHandler()

  def ListFlowOutputPlugins(self, args, token=None):
    return api_flow.ApiListFlowOutputPluginsHandler()

  def ListFlowOutputPluginLogs(self, args, token=None):
    return api_flow.ApiListFlowOutputPluginLogsHandler()

  def ListFlowOutputPluginErrors(self, args, token=None):
    return api_flow.ApiListFlowOutputPluginErrorsHandler()

  def ListFlowLogs(self, args, token=None):
    return api_flow.ApiListFlowLogsHandler()

  # Global flows methods.
  # ====================
  #
  def CreateGlobalFlow(self, args, token=None):
    # TODO(user): split global- and client- flows creation handlers.
    return api_flow.ApiCreateFlowHandler()

  # Cron jobs methods.
  # =================
  #
  def ListCronJobs(self, args, token=None):
    return api_cron.ApiListCronJobsHandler()

  def CreateCronJob(self, args, token=None):
    return api_cron.ApiCreateCronJobHandler()

  # Hunts methods.
  # =============
  #
  def ListHunts(self, args, token=None):
    return api_hunt.ApiListHuntsHandler()

  def GetHunt(self, args, token=None):
    return api_hunt.ApiGetHuntHandler()

  def ListHuntErrors(self, args, token=None):
    return api_hunt.ApiListHuntErrorsHandler()

  def ListHuntLogs(self, args, token=None):
    return api_hunt.ApiListHuntLogsHandler()

  def ListHuntResults(self, args, token=None):
    return api_hunt.ApiListHuntResultsHandler()

  def GetHuntResultsExportCommand(self, args, token=None):
    return api_hunt.ApiGetHuntResultsExportCommandHandler()

  def ListHuntOutputPlugins(self, args, token=None):
    return api_hunt.ApiListHuntOutputPluginsHandler()

  def ListHuntOutputPluginLogs(self, args, token=None):
    return api_hunt.ApiListHuntOutputPluginLogsHandler()

  def ListHuntOutputPluginErrors(self, args, token=None):
    return api_hunt.ApiListHuntOutputPluginErrorsHandler()

  def ListHuntCrashes(self, args, token=None):
    return api_hunt.ApiListHuntCrashesHandler()

  def GetClientCompletionStats(self, args, token=None):
    return api_hunt.ApiGetClientCompletionStatsHandler()

  def GetHuntStats(self, args, token=None):
    return api_hunt.ApiGetHuntStatsHandler()

  def GetHuntClients(self, args, token=None):
    return api_hunt.ApiGetHuntClientsHandler()

  def GetHuntContext(self, args, token=None):
    return api_hunt.ApiGetHuntContextHandler()

  def CreateHunt(self, args, token=None):
    return api_hunt.ApiCreateHuntHandler()

  def GetHuntFilesArchive(self, args, token=None):
    return api_hunt.ApiGetHuntFilesArchiveHandler()

  def GetHuntFile(self, args, token=None):
    return api_hunt.ApiGetHuntFileHandler()

  # Stats metrics methods.
  # =====================
  #
  def ListStatsStoreMetricsMetadata(self, args, token=None):
    return api_stats.ApiListStatsStoreMetricsMetadataHandler()

  def GetStatsStoreMetric(self, args, token=None):
    return api_stats.ApiGetStatsStoreMetricHandler()

  # Approvals methods.
  # =================
  #
  def CreateUserClientApproval(self, args, token=None):
    return api_user.ApiCreateUserClientApprovalHandler()

  def GetUserClientApproval(self, args, token=None):
    return api_user.ApiGetUserClientApprovalHandler()

  def ListUserClientApprovals(self, args, token=None):
    return api_user.ApiListUserClientApprovalsHandler()

  def ListUserHuntApprovals(self, args, token=None):
    return api_user.ApiListUserHuntApprovalsHandler()

  def ListUserCronApprovals(self, args, token=None):
    return api_user.ApiListUserCronApprovalsHandler()

  # User settings methods.
  # =====================
  #
  def GetUserInfo(self, args, token=None):
    return api_user.ApiGetUserInfoHandler()

  def GetPendingUserNotificationsCount(self, args, token=None):
    return api_user.ApiGetPendingUserNotificationsCountHandler()

  def GetPendingUserNotifications(self, args, token=None):
    return api_user.ApiGetPendingUserNotificationsHandler()

  def DeletePendingUserNotification(self, args, token=None):
    return api_user.ApiDeletePendingUserNotificationHandler()

  def GetAndResetUserNotifications(self, args, token=None):
    return api_user.ApiGetAndResetUserNotificationsHandler()

  def GetUserSettings(self, args, token=None):
    return api_user.ApiGetUserSettingsHandler()

  def UpdateUserSettings(self, args, token=None):
    return api_user.ApiUpdateUserSettingsHandler()

  # Config methods.
  # ==============
  #
  def GetConfig(self, args, token=None):
    return api_config.ApiGetConfigHandler()

  def GetConfigOption(self, args, token=None):
    return api_config.ApiGetConfigOptionHandler()

  # Reflection methods.
  # ==================
  #
  def ListKbFields(self, args, token=None):
    return api_client.ApiListKbFieldsHandler()

  def ListFlowDescriptors(self, args, token=None):
    # TODO(user): move to reflection.py
    return api_flow.ApiListFlowDescriptorsHandler()

  def ListAff4AttributeDescriptors(self, args, token=None):
    return api_reflection.ApiListAff4AttributesDescriptorsHandler()

  def GetRDFValueDescriptor(self, args, token=None):
    return api_reflection.ApiGetRDFValueDescriptorHandler()

  def ListRDFValuesDescriptors(self, args, token=None):
    return api_reflection.ApiListRDFValuesDescriptorsHandler()

  def ListOutputPluginDescriptors(self, args, token=None):
    return api_output_plugin.ApiOutputPluginsListHandler()

  def ListKnownEncodings(self, args, token=None):
    return api_vfs.ApiListKnownEncodingsHandler()

  # Documentation methods.
  # =====================
  #
  def GetDocs(self, args, token=None):
    return api_docs.ApiGetDocsHandler()

  # Robot methods (methods that provide limited access to the system and
  # are supposed to be triggered by the scripts).
  # ====================================================================
  #
  def StartGetFileOperation(self, args, token=None):
    return api_flow.ApiStartGetFileOperationHandler()

  # Note: the difference between GetFlow and GetFlowStatus is that
  # GetFlowStatus shouldn't require an approval or any other form
  # of authorization to work.
  def GetFlowStatus(self, args, token=None):
    return api_flow.ApiGetFlowStatusHandler()
