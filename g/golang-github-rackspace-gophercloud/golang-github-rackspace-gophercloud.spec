Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
# END SourceDeps(oneline)
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
# Two following test passes but it is about 50% of all.
# Some tests fails, some fails on build failure
# Besides, BuildRequires is not complete as there is a cyclic deps with smashwilson/gophercloud
%global with_check 0
# Generate unit-test rpm
%global with_unit_test 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider        github
%global provider_tld    com
%global project         rackspace
%global repo            gophercloud
# https://github.com/rackspace/gophercloud
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          c90cb954266e1bdd6d1914678fd6909fc5fabbfa
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        1.0.0
Release:        alt1_17
Summary:        The Go SDK for Openstack http://gophercloud.io
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
Source44: import.info

%description
Gophercloud currently lets you authenticate with OpenStack providers to create
and manage servers. We are working on extending the API to further include
cloud files, block storage, DNS, databases, security groups,
and other features.

This library is still in the very early stages of development.

%if 0%{?with_devel}
%package devel
Group: Development/Other
Summary:       %{summary}
BuildArch:     noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/mitchellh/mapstructure)
BuildRequires: golang(gopkg.in/yaml.v2)
%endif

Requires:      golang(github.com/mitchellh/mapstructure)
Requires:      golang(gopkg.in/yaml.v2)

Provides:      golang(%{import_path}) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/blockstorage/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/blockstorage/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/blockstorage/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/compute/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/db/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/identity/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/identity/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/imageservice/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2/extensions/fwaas) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2/extensions/lbaas) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2/extensions/lbaas_v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/networking/v2/extensions/portsbinding) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/objectstorage/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/openstack/orchestration/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/blockstorage/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/cdn/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/compute/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/db/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/identity/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/lb/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/networking/v2) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/objectstorage/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/orchestration/v1) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/rackspace/rackconnect/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/acceptance/tools) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v1/apiversions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v1/snapshots) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v1/volumes) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v1/volumes/testing) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v1/volumetypes) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v2/extensions/volumeactions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/blockstorage/v2/volumes) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/cdn/v1/base) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/cdn/v1/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/cdn/v1/serviceassets) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/cdn/v1/services) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/common/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/adminactions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/bootfromvolume) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/defsecrules) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/diskconfig) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/floatingip) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/keypairs) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/networks) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/quotasets) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/schedulerhints) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/secgroups) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/servergroups) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/startstop) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/tenantnetworks) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/volumeattach) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/extensions/volumeattach/testing) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/images) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/compute/v2/servers) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/configurations) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/databases) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/datastores) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/instances) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/db/v1/users) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v2/extensions/admin/roles) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v2/tenants) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v2/tokens) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v2/users) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/endpoints) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/extensions/trust) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/roles) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/services) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/identity/v3/tokens) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/imageservice/v2/images) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/imageservice/v2/members) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/apiversions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/common) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/external) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/fwaas) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/fwaas/firewalls) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/fwaas/policies) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/fwaas/rules) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/layer3) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/layer3/floatingips) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/layer3/routers) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas/members) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas/monitors) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas/pools) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas/vips) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas_v2) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas_v2/listeners) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas_v2/loadbalancers) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas_v2/monitors) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/lbaas_v2/pools) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/portsbinding) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/provider) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/security) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/security/groups) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/extensions/security/rules) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/networks) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/ports) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/networking/v2/subnets) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/objectstorage/v1/accounts) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/objectstorage/v1/containers) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/objectstorage/v1/objects) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/apiversions) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/buildinfo) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/stackevents) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/stackresources) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/stacks) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/orchestration/v1/stacktemplates) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/telemetry/v2/meters) = %{version}-%{release}
Provides:      golang(%{import_path}/openstack/utils) = %{version}-%{release}
Provides:      golang(%{import_path}/pagination) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/autoscale/v1/policies) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/autoscale/v1/webhooks) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/blockstorage/v1/snapshots) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/blockstorage/v1/volumes) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/blockstorage/v1/volumetypes) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/cdn/v1/base) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/cdn/v1/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/cdn/v1/serviceassets) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/cdn/v1/services) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/bootfromvolume) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/images) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/keypairs) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/networks) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/servers) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/virtualinterfaces) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/compute/v2/volumeattach) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/backups) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/configurations) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/databases) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/datastores) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/flavors) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/instances) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/db/v1/users) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/identity/v2/extensions) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/identity/v2/roles) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/identity/v2/tenants) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/identity/v2/tokens) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/identity/v2/users) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/acl) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/lbs) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/monitors) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/nodes) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/sessions) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/ssl) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/throttle) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/lb/v1/vips) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/common) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/networks) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/ports) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/security) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/security/groups) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/security/rules) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/networking/v2/subnets) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/accounts) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/bulk) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/cdncontainers) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/cdnobjects) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/containers) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/objectstorage/v1/objects) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/orchestration/v1/buildinfo) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/orchestration/v1/stackevents) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/orchestration/v1/stackresources) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/orchestration/v1/stacks) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/orchestration/v1/stacktemplates) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/rackconnect/v3) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/rackconnect/v3/cloudnetworks) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/rackconnect/v3/lbpools) = %{version}-%{release}
Provides:      golang(%{import_path}/rackspace/rackconnect/v3/publicips) = %{version}-%{release}
Provides:      golang(%{import_path}/testhelper) = %{version}-%{release}
Provides:      golang(%{import_path}/testhelper/client) = %{version}-%{release}
Provides:      golang(%{import_path}/testhelper/fixture) = %{version}-%{release}

%description devel
Gophercloud currently lets you authenticate with OpenStack providers to create 
and manage servers. We are working on extending the API to further include 
cloud files, block storage, DNS, databases, security groups, 
and other features.

This library is still in the very early stages of development.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test}
%package unit-test
Group: Development/Other
Summary:         Unit tests for %{name} package

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
BuildRequires: golang(golang.org/x/crypto/ssh)
%endif

# test subpackage tests code from devel subpackage

Requires: golang(golang.org/x/crypto/ssh)

%description unit-test
%{summary}

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
echo "%%dir %%{go_path}/src/%%{import_path}/." >> devel.file-list
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go") ; do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> devel.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> devel.file-list.dir
    done
done
sort -u devel.file-list.dir >> devel.file-list
%endif

# testing files for this project
%if 0%{?with_unit_test}
install -d -p %{buildroot}/%{go_path}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go"); do
    install -d -p %{buildroot}/%{go_path}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{go_path}/src/%{import_path}/$file
    echo "%%{go_path}/src/%%{import_path}/$file" >> unit-test.file-list
    filedir=${file##./};
    # note %%%% -> %% for rpm macros!
    while [ ${filedir%%/*} != "$filedir" ]; do
        filedir=${filedir%%/*}
	echo "%%dir %%{go_path}/src/%%{import_path}/$filedir" >> unit-test.file-list.dir
    done
done
sort -u unit-test.file-list.dir >> unit-test.file-list
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

%gotest %{import_path}
%gotest %{import_path}/acceptance/openstack
%gotest %{import_path}/acceptance/openstack/blockstorage/v1
%gotest %{import_path}/acceptance/openstack/compute/v2
%gotest %{import_path}/acceptance/openstack/identity/v2
%gotest %{import_path}/acceptance/openstack/identity/v3
%gotest %{import_path}/acceptance/openstack/networking/v2
%gotest %{import_path}/acceptance/openstack/networking/v2/extensions
%gotest %{import_path}/acceptance/openstack/networking/v2/extensions/fwaas
%gotest %{import_path}/acceptance/openstack/networking/v2/extensions/lbaas
%gotest %{import_path}/acceptance/openstack/objectstorage/v1
%gotest %{import_path}/acceptance/openstack/orchestration/v1
%gotest %{import_path}/acceptance/rackspace
%gotest %{import_path}/acceptance/rackspace/blockstorage/v1
%gotest %{import_path}/acceptance/rackspace/cdn/v1
%gotest %{import_path}/acceptance/rackspace/compute/v2
%gotest %{import_path}/acceptance/rackspace/identity/v2
%gotest %{import_path}/acceptance/rackspace/lb/v1
%gotest %{import_path}/acceptance/rackspace/networking/v2
%gotest %{import_path}/acceptance/rackspace/objectstorage/v1
%gotest %{import_path}/acceptance/rackspace/orchestration/v1
%gotest %{import_path}/acceptance/rackspace/rackconnect/v3
%gotest %{import_path}/openstack
%gotest %{import_path}/openstack/blockstorage/v1/apiversions
%gotest %{import_path}/openstack/blockstorage/v1/snapshots
%gotest %{import_path}/openstack/blockstorage/v1/volumes
%gotest %{import_path}/openstack/blockstorage/v1/volumetypes
%gotest %{import_path}/openstack/cdn/v1/base
%gotest %{import_path}/openstack/cdn/v1/flavors
%gotest %{import_path}/openstack/cdn/v1/serviceassets
%gotest %{import_path}/openstack/cdn/v1/services
%gotest %{import_path}/openstack/common/extensions
%gotest %{import_path}/openstack/compute/v2/extensions
%gotest %{import_path}/openstack/compute/v2/extensions/bootfromvolume
%gotest %{import_path}/openstack/compute/v2/extensions/defsecrules
%gotest %{import_path}/openstack/compute/v2/extensions/diskconfig
%gotest %{import_path}/openstack/compute/v2/extensions/floatingip
%gotest %{import_path}/openstack/compute/v2/extensions/keypairs
%gotest %{import_path}/openstack/compute/v2/extensions/secgroups
%gotest %{import_path}/openstack/compute/v2/extensions/servergroups
%gotest %{import_path}/openstack/compute/v2/extensions/startstop
%gotest %{import_path}/openstack/compute/v2/extensions/tenantnetworks
%gotest %{import_path}/openstack/compute/v2/extensions/volumeattach
%gotest %{import_path}/openstack/compute/v2/flavors
%gotest %{import_path}/openstack/compute/v2/images
%gotest %{import_path}/openstack/compute/v2/servers
%gotest %{import_path}/openstack/identity/v2/extensions
%gotest %{import_path}/openstack/identity/v2/extensions/admin/roles
%gotest %{import_path}/openstack/identity/v2/tenants
%gotest %{import_path}/openstack/identity/v2/tokens
%gotest %{import_path}/openstack/identity/v2/users
%gotest %{import_path}/openstack/identity/v3/endpoints
%gotest %{import_path}/openstack/identity/v3/services
%gotest %{import_path}/openstack/identity/v3/tokens
%gotest %{import_path}/openstack/networking/v2/apiversions
%gotest %{import_path}/openstack/networking/v2/extensions
%gotest %{import_path}/openstack/networking/v2/extensions/external
%gotest %{import_path}/openstack/networking/v2/extensions/fwaas/firewalls
%gotest %{import_path}/openstack/networking/v2/extensions/fwaas/policies
%gotest %{import_path}/openstack/networking/v2/extensions/fwaas/rules
%gotest %{import_path}/openstack/networking/v2/extensions/layer3/floatingips
%gotest %{import_path}/openstack/networking/v2/extensions/layer3/routers
%gotest %{import_path}/openstack/networking/v2/extensions/lbaas/members
%gotest %{import_path}/openstack/networking/v2/extensions/lbaas/monitors
%gotest %{import_path}/openstack/networking/v2/extensions/lbaas/pools
%gotest %{import_path}/openstack/networking/v2/extensions/lbaas/vips
%gotest %{import_path}/openstack/networking/v2/extensions/provider
%gotest %{import_path}/openstack/networking/v2/extensions/security/groups
%gotest %{import_path}/openstack/networking/v2/extensions/security/rules
%gotest %{import_path}/openstack/networking/v2/networks
%gotest %{import_path}/openstack/networking/v2/ports
%gotest %{import_path}/openstack/networking/v2/subnets
%gotest %{import_path}/openstack/objectstorage/v1/accounts
%gotest %{import_path}/openstack/objectstorage/v1/containers
%gotest %{import_path}/openstack/objectstorage/v1/objects
%gotest %{import_path}/openstack/orchestration/v1/apiversions
%gotest %{import_path}/openstack/orchestration/v1/buildinfo
%gotest %{import_path}/openstack/orchestration/v1/stackevents
%gotest %{import_path}/openstack/orchestration/v1/stackresources
%gotest %{import_path}/openstack/orchestration/v1/stacks
%gotest %{import_path}/openstack/orchestration/v1/stacktemplates
%gotest %{import_path}/openstack/utils
%gotest %{import_path}/pagination
%gotest %{import_path}/rackspace
%gotest %{import_path}/rackspace/blockstorage/v1/snapshots
%gotest %{import_path}/rackspace/blockstorage/v1/volumes
%gotest %{import_path}/rackspace/blockstorage/v1/volumetypes
%gotest %{import_path}/rackspace/cdn/v1/base
%gotest %{import_path}/rackspace/cdn/v1/flavors
%gotest %{import_path}/rackspace/cdn/v1/serviceassets
%gotest %{import_path}/rackspace/cdn/v1/services
%gotest %{import_path}/rackspace/compute/v2/bootfromvolume
%gotest %{import_path}/rackspace/compute/v2/flavors
%gotest %{import_path}/rackspace/compute/v2/images
%gotest %{import_path}/rackspace/compute/v2/keypairs
%gotest %{import_path}/rackspace/compute/v2/networks
%gotest %{import_path}/rackspace/compute/v2/servers
%gotest %{import_path}/rackspace/compute/v2/virtualinterfaces
%gotest %{import_path}/rackspace/compute/v2/volumeattach
%gotest %{import_path}/rackspace/identity/v2/extensions
%gotest %{import_path}/rackspace/identity/v2/roles
%gotest %{import_path}/rackspace/identity/v2/tenants
%gotest %{import_path}/rackspace/identity/v2/tokens
%gotest %{import_path}/rackspace/identity/v2/users
%gotest %{import_path}/rackspace/lb/v1/acl
%gotest %{import_path}/rackspace/lb/v1/lbs
%gotest %{import_path}/rackspace/lb/v1/monitors
%gotest %{import_path}/rackspace/lb/v1/nodes
%gotest %{import_path}/rackspace/lb/v1/sessions
%gotest %{import_path}/rackspace/lb/v1/ssl
%gotest %{import_path}/rackspace/lb/v1/throttle
%gotest %{import_path}/rackspace/lb/v1/vips
%gotest %{import_path}/rackspace/networking/v2/networks
%gotest %{import_path}/rackspace/networking/v2/ports
%gotest %{import_path}/rackspace/networking/v2/security/groups
%gotest %{import_path}/rackspace/networking/v2/security/rules
%gotest %{import_path}/rackspace/networking/v2/subnets
%gotest %{import_path}/rackspace/objectstorage/v1/accounts
%gotest %{import_path}/rackspace/objectstorage/v1/bulk
%gotest %{import_path}/rackspace/objectstorage/v1/cdncontainers
%gotest %{import_path}/rackspace/objectstorage/v1/cdnobjects
%gotest %{import_path}/rackspace/objectstorage/v1/containers
%gotest %{import_path}/rackspace/objectstorage/v1/objects
%gotest %{import_path}/rackspace/orchestration/v1/buildinfo
%gotest %{import_path}/rackspace/orchestration/v1/stackevents
%gotest %{import_path}/rackspace/orchestration/v1/stackresources
%gotest %{import_path}/rackspace/orchestration/v1/stacks
%gotest %{import_path}/rackspace/orchestration/v1/stacktemplates
%gotest %{import_path}/rackspace/rackconnect/v3/cloudnetworks
%gotest %{import_path}/rackspace/rackconnect/v3/lbpools
%gotest %{import_path}/rackspace/rackconnect/v3/publicips
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%if 0%{?with_devel}
%files devel -f devel.file-list
%doc LICENSE
%doc README.md CONTRIBUTING.md UPGRADING.md CONTRIBUTORS.md
%dir %{go_path}/src/%{provider}.%{provider_tld}/%{project}
%endif

%if 0%{?with_unit_test}
%files unit-test -f unit-test.file-list
%doc LICENSE
%endif

%changelog
* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_17
- new version

