Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# If any of the following macros should be set otherwise,
# you can wrap any of them with the following conditions:
# - %%if 0%%{centos} == 7
# - %%if 0%%{?rhel} == 7
# - %%if 0%%{?fedora} == 23
# Or just test for particular distribution:
# - %%if 0%%{centos}
# - %%if 0%%{?rhel}
# - %%if 0%%{?fedora}
#
# Be aware, on centos, both %%rhel and %%centos are set. If you want to test
# rhel specific macros, you can use %%if 0%%{?rhel} && 0%%{?centos} == 0 condition.
# (Don't forget to replace double percentage symbol with single one in order to apply a condition)

# Generate devel rpm
%global with_devel 1
# Build project from bundled dependencies
%global with_bundled 0
# Build with debug info rpm
%global with_debug 0
# Run tests in check section
%global with_check 1
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         google
%global repo            google-api-go-client
# https://github.com/google/google-api-go-client
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     google.golang.org/api
%global commit          77f162b8178853926ec7d7673e1aa77f8128517a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global gg_name         golang-google-golang-api

%global gc_rev             e1c259484b495133836706f46319f5897f1e9bf6
%global gc_shortrev        %(r=%{gc_rev}; echo ${r:0:12})
%global gc_provider        google
%global gc_provider_sub    code
%global gc_provider_tld    com
%global gc_repo            google-api-go-client
# code.google.com/p/google-api-go-client
%global gc_import_path     %{gc_provider_sub}.%{gc_provider}.%{gc_provider_tld}/p/%{gc_repo}
%global gc_name            golang-%{gc_provider}%{gc_provider_sub}-%{gc_repo}

%global devel_main         %{gg_name}-devel

Name:           golang-googlecode-google-api-client
Version:        0
Release:        alt1_0.20.git%{shortcommit}
Summary:        Go libraries for "new style" Google APIs
License:        BSD
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/google-api-go-client-%{shortcommit}.tar.gz
Source1:        https://%{gc_repo}.%{gc_provider}%{gc_provider_sub}.%{gc_provider_tld}/archive/%{gc_rev}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
%{summary}

%if 0%{?with_devel}
%package -n %{gc_name}-devel
Group: Development/Other
Summary:        Go libraries for "new style" Google APIs
BuildArch:      noarch

Provides: golang(%{gc_import_path}/adexchangebuyer/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/directory_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/email_migration_v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/admin/reports_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsense/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v2.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/analytics/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/androidpublisher/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appsactivity/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/appstate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/audit/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/bigquery/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/blogger/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/books/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/calendar/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/us_v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/civicinfo/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/cloudmonitoring/v2beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/compute/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/content/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/coordinate/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/customsearch/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/datastore/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/discovery/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/dns/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/drive/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1-sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/freebase/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/games/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gan/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/genomics/v1beta) = %{version}-%{release}
Provides: golang(%{gc_import_path}/gmail/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/google-api-go-generator) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/internal/uritemplates) = %{version}-%{release}
Provides: golang(%{gc_import_path}/googleapi/transport) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupsmigration/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/groupssettings/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/licensing/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/manager/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/exp2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mapsengine/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/mirror/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/oauth2/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/orkut/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plus/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/plusdomains/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.4) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.5) = %{version}-%{release}
Provides: golang(%{gc_import_path}/prediction/v1.6) = %{version}-%{release}
Provides: golang(%{gc_import_path}/pubsub/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/qpxexpress/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides: golang(%{gc_import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/siteverification/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/storage/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/tasks/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/translate/v2) = %{version}-%{release}
Provides: golang(%{gc_import_path}/urlshortener/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/webfonts/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtube/v3) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides: golang(%{gc_import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}

%description -n %{gc_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 

%package -n %{gg_name}-devel
Group: Development/Other
Summary:        Go libraries for "new style" Google APIs
BuildArch:      noarch

%if 0%{?with_check}
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(google.golang.org/appengine/socket)
BuildRequires: golang(google.golang.org/appengine/urlfetch)
BuildRequires: golang(google.golang.org/genproto/googleapis/bytestream)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/codes)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/credentials/oauth)
BuildRequires: golang(google.golang.org/grpc/naming)
%endif

Requires:       golang(golang.org/x/net/context)
Requires:       golang(golang.org/x/net/context/ctxhttp)
Requires:       golang(golang.org/x/oauth2)
Requires:       golang(golang.org/x/oauth2/google)
Requires:       golang(google.golang.org/appengine/socket)
Requires:       golang(google.golang.org/appengine/urlfetch)
Requires:       golang(google.golang.org/genproto/googleapis/bytestream)
Requires:       golang(google.golang.org/grpc)
Requires:       golang(google.golang.org/grpc/codes)
Requires:       golang(google.golang.org/grpc/credentials)
Requires:       golang(google.golang.org/grpc/credentials/oauth)
Requires:       golang(google.golang.org/grpc/naming)

Provides:       golang(%{import_path}/acceleratedmobilepageurl/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangebuyer2/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/adexchangeseller/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/datatransfer/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/directory/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/email_migration/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/admin/reports/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/adsense/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/adsensehost/v4.1) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/analytics/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/analyticsreporting/v4) = %{version}-%{release}
Provides:       golang(%{import_path}/androidenterprise/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/androidpublisher/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1beta) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1beta4) = %{version}-%{release}
Provides:       golang(%{import_path}/appengine/v1beta5) = %{version}-%{release}
Provides:       golang(%{import_path}/appsactivity/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/appstate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/autoscaler/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/bigquery/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/blogger/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/books/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/calendar/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/civicinfo/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/classroom/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudbilling/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudbuild/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/clouddebugger/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/clouderrorreporting/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudkms/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudlatencytest/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudmonitoring/v2beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudresourcemanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudresourcemanager/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/cloudtrace/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/v0.beta) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/vm_alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/clouduseraccounts/vm_beta) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v0.beta) = %{version}-%{release}
Provides:       golang(%{import_path}/compute/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/consumersurveys/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/container/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/content/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/content/v2sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/coordinate/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/customsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dataflow/v1b3) = %{version}-%{release}
Provides:       golang(%{import_path}/dataproc/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dataproc/v1alpha1) = %{version}-%{release}
Provides:       golang(%{import_path}/dataproc/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/datastore/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/deploymentmanager/v2beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.0) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.2) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.3) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.4) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.5) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.5beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.6) = %{version}-%{release}
Provides:       golang(%{import_path}/dfareporting/v2.7) = %{version}-%{release}
Provides:       golang(%{import_path}/discovery/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/dns/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclickbidmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/doubleclicksearch/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/drive/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/firebasedynamiclinks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/firebaserules/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/fitness/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/freebase/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/fusiontables/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/fusiontables/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/games/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesconfiguration/v1configuration) = %{version}-%{release}
Provides:       golang(%{import_path}/gamesmanagement/v1management) = %{version}-%{release}
Provides:       golang(%{import_path}/gan/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1alpha2) = %{version}-%{release}
Provides:       golang(%{import_path}/genomics/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/gensupport) = %{version}-%{release}
Provides:       golang(%{import_path}/gmail/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi) = %{version}-%{release}
Provides:       golang(%{import_path}/googleapi/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/groupsmigration/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/groupssettings/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/iam/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/iam/v1alpha1) = %{version}-%{release}
Provides:       golang(%{import_path}/identitytoolkit/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/iterator) = %{version}-%{release}
Provides:       golang(%{import_path}/iterator/testing) = %{version}-%{release}
Provides:       golang(%{import_path}/kgsearch/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/language/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/language/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/licensing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/logging/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/logging/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/logging/v2beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/manager/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/manufacturers/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/exp2) = %{version}-%{release}
Provides:       golang(%{import_path}/mapsengine/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/mirror/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/ml/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/monitoring/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/oauth2/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/option) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/pagespeedonline/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/partners/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/people/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/playmoviespartner/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plus/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/plusdomains/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.2) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.3) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.4) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.5) = %{version}-%{release}
Provides:       golang(%{import_path}/prediction/v1.6) = %{version}-%{release}
Provides:       golang(%{import_path}/proximitybeacon/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta1a) = %{version}-%{release}
Provides:       golang(%{import_path}/pubsub/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/qpxexpress/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapool/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/replicapoolupdater/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/reseller/v1sandbox) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/resourceviews/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/runtimeconfig/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/runtimeconfig/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/safebrowsing/v4) = %{version}-%{release}
Provides:       golang(%{import_path}/script/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/searchconsole/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/servicecontrol/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/servicemanagement/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/serviceregistry/v0.alpha) = %{version}-%{release}
Provides:       golang(%{import_path}/serviceuser/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/sheets/v4) = %{version}-%{release}
Provides:       golang(%{import_path}/siteverification/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/slides/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/sourcerepo/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/spanner/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/spectrum/v1explorer) = %{version}-%{release}
Provides:       golang(%{import_path}/speech/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/sqladmin/v1beta4) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/storage/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/storagetransfer/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/support/bundler) = %{version}-%{release}
Provides:       golang(%{import_path}/surveys/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/tagmanager/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/taskqueue/v1beta2) = %{version}-%{release}
Provides:       golang(%{import_path}/tasks/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/toolresults/v1beta3) = %{version}-%{release}
Provides:       golang(%{import_path}/toolresults/v1beta3firstparty) = %{version}-%{release}
Provides:       golang(%{import_path}/tracing/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/translate/v2) = %{version}-%{release}
Provides:       golang(%{import_path}/transport) = %{version}-%{release}
Provides:       golang(%{import_path}/transport/bytestream) = %{version}-%{release}
Provides:       golang(%{import_path}/urlshortener/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/vision/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webfonts/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/webmasters/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtube/v3) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubeanalytics/v1beta1) = %{version}-%{release}
Provides:       golang(%{import_path}/youtubereporting/v1) = %{version}-%{release}

%description -n %{gg_name}-devel
%{summary}

These are auto-generated Go libraries from the Google Discovery Services JSON
description files of the available "new style" Google APIs.

Announcement email:
http://groups.google.com/group/golang-nuts/browse_thread/thread/6c7281450be9a21e

Status: Relative to the other Google API clients, this library is labeled alpha.
Some advanced features may not work. Please file bugs if any problems are found.

Getting started documentation:
    http://code.google.com/p/google-api-go-client/wiki/GettingStarted 
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test-devel
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage

%if 0%{?with_check} && ! 0%{?with_bundled}
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
%endif

Requires:      golang(golang.org/x/oauth2)
Requires:      golang(golang.org/x/oauth2/google)

%description unit-test-devel
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{gc_repo}-%{gc_shortrev} -T -b 1
%setup -q -n google-api-go-client-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/
echo "%%dir %%{go_path}/src/%%{gc_import_path}/." >> gc_devel.file-list
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
pushd ../%{gc_repo}-%{gc_shortrev}
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{gc_import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{gc_import_path}/$file
    echo "%%{go_path}/src/%%{gc_import_path}/$file" >> ../google-api-go-client-%{commit}/gc_devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{gc_import_path}/$filedir" >> ../google-api-go-client-%{commit}/gc_devel.file-list.dir
    done
done
[ -s ../google-api-go-client-%{commit}/gc_devel.file-list.dir ] && sort -u ../google-api-go-client-%{commit}/gc_devel.file-list.dir >> ../google-api-go-client-%{commit}/gc_devel.file-list
rm -f ../google-api-go-client-%{commit}/gc_devel.file-list.dir
popd
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    dirprefix=$(dirname $file)
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$dirprefix
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list

    while [ "$dirprefix" != "." ]; do
        echo "%%dir %%{go_path}/src/%%{import_path}/$dirprefix" >> devel.file-list
        dirprefix=$(dirname $dirprefix)
    done
done
for file in $(find ./google-api-go-generator/testdata/ -iname "*"); do
    if [ "$file" == "./google-api-go-generator/testdata/" ]; then
        continue
    fi
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test-devel.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{go_path}:%{go_path}
%else
export GOPATH=%{buildroot}/%{go_path}:$(pwd)/Godeps/_workspace:%{go_path}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

%gotest %{import_path}/gensupport
%gotest %{import_path}/google-api-go-generator
%gotest %{import_path}/googleapi
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files -n %{gg_name}-devel -f devel.file-list
%doc LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md

%files -n %{gc_name}-devel -f gc_devel.file-list
%doc LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test-devel -f unit-test-devel.file-list
%doc LICENSE
%doc AUTHORS CONTRIBUTORS NOTES README.md TODO CONTRIBUTING.md
%endif

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.20.git77f162b
- new version

