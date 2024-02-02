%define        _unpackaged_files_terminate_build 1

Name:          azure-sdk-for-python
Version:       20230815
Release:       alt1

Summary:       Azure SDK for Python
License:       MIT
Group:         Development/Python3
Url:           https://azure.github.io/azure-sdk-for-python/
Vcs:           https://github.com/Azure/azure-sdk-for-python.git

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel

BuildArch:     noarch
Source:        %name-%version.tar

%description
Azure SDK for Python

Packages Dependencies DepGraph Python Build Status

This repository is for active development of the Azure SDK for Python. For
consumers of the SDK we recommend visiting our public developer docs or our
versioned developer docs.

%package       -n python3-module-azure-core
Version:       1.29.2
Release:       alt1
Summary:       Azure Core shared client library for Python
Group:         Development/Python3

%description   -n python3-module-azure-core
Azure Core shared client library for Python.

Azure core provides shared exceptions and modules for Python SDK client
libraries. These libraries follow the Azure SDK Design Guidelines for Python.

If you are a client library developer, please reference client library developer
reference for more information.


%package       -n python3-module-azure-common
Version:       1.1.28
Release:       alt1
Summary:       Microsoft Azure Client Library for Python (Common)
Group:         Development/Python3

%description   -n python3-module-azure-common
Microsoft Azure Client Library for Python (Common).

This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.


%package       -n python3-module-azure-mgmt-core
Version:       1.4.0
Release:       alt1
Summary:       Microsoft Azure Management Core Library for Python
Group:         Development/Python3

%description   -n python3-module-azure-mgmt-core
Microsoft Azure Management Core Library for Python.

Azure management core library defines extensions to Azure Core that are specific
to ARM (Azure Resource Management) needed when you use client libraries.

As an end user, you don't need to manually install azure-mgmt-core because it
will be installed automatically when you install other SDKs.

%package       -n python3-module-azure-identity
Version:       1.14.0
Release:       alt1
Summary:       Microsoft Azure Identity Library for Python
Group:         Development/Python3

%description   -n python3-module-azure-identity
Microsoft Azure Identity Library for Python

The Azure Identity library provides Azure Active Directory (Azure AD) token
authentication support across the Azure SDK. It provides a set of
TokenCredential implementations, which can be used to construct Azure SDK
clients that support Azure AD token authentication.


%package       -n python3-module-azure-mgmt-rdbms
Version:       10.2.0b3
Release:       alt1
Summary:       Microsoft Azure RDBMS Management Client Library for Python
Group:         Development/Python3

%description   -n python3-module-azure-mgmt-rdbms
Microsoft Azure RDBMS Management Client Library for Python.

This is the Microsoft Azure RDBMS Management Client Library. This package has
been tested with Python 3.7+. For a more complete view of Azure libraries, see
the azure sdk python release.


%package       -n python3-module-azure-mgmt-resource
Version:       23.1.0b2
Release:       alt1
Summary:       Microsoft Azure Resource Management Client Library for Python
Group:         Development/Python3

%description   -n python3-module-azure-mgmt-resource
Microsoft Azure Resource Management Client Library for Python.

This is the Microsoft Azure Resource Management Client Library. This package has
been tested with Python 3.7+. For a more complete view of Azure libraries, see
the azure sdk python release.


%package       -n python3-module-azure-mgmt-subscription
Version:       3.1.1
Release:       alt1
Summary:       Microsoft Azure Subscription Management Client Library for Python
Group:         Development/Python3

%description   -n python3-module-azure-mgmt-subscription
Microsoft Azure Subscription Management Client Library for Python.

This is the Microsoft Azure Subscription Management Client Library. This package
has been tested with Python 3.7+. For a more complete view of Azure libraries,
see the azure sdk python release.


%prep
%setup

%build
pushd sdk/core/azure-core
%pyproject_build
popd
pushd sdk/core/azure-common
%pyproject_build
popd
pushd sdk/core/azure-mgmt-core
%pyproject_build
popd
pushd sdk/identity/azure-identity
%pyproject_build
popd
pushd sdk/rdbms/azure-mgmt-rdbms
%pyproject_build
popd
pushd sdk/resources/azure-mgmt-resource
%pyproject_build
popd
pushd sdk/subscription/azure-mgmt-subscription
%pyproject_build
popd

%install
pushd sdk/core/azure-core
%pyproject_install
popd
pushd sdk/core/azure-common
%pyproject_install
popd
pushd sdk/core/azure-mgmt-core
%pyproject_install
popd
pushd sdk/identity/azure-identity
%pyproject_install
popd
pushd sdk/rdbms/azure-mgmt-rdbms
%pyproject_install
popd
pushd sdk/resources/azure-mgmt-resource
%pyproject_install
popd
pushd sdk/subscription/azure-mgmt-subscription
%pyproject_install
popd


%files
%doc *.rst

%files         -n python3-module-azure-core
%doc *.rst sdk/core/azure-core/README.md
%python3_sitelibdir/azure/core
%python3_sitelibdir/azure_core*

%files         -n python3-module-azure-common
%doc *.rst sdk/core/azure-common/README.md
%python3_sitelibdir/azure/common
%python3_sitelibdir/azure/profiles
%python3_sitelibdir/azure_common*

%files         -n python3-module-azure-mgmt-core
%doc *.rst sdk/core/azure-mgmt-core/README.md
%python3_sitelibdir/azure/mgmt/core
%python3_sitelibdir/azure_mgmt_core*

%files         -n python3-module-azure-identity
%doc *.rst sdk/identity/azure-identity/README.md
%python3_sitelibdir/azure/identity
%python3_sitelibdir/azure_identity*

%files         -n python3-module-azure-mgmt-rdbms
%doc *.rst sdk/rdbms/azure-mgmt-rdbms/README.md
%python3_sitelibdir/azure/mgmt/rdbms
%python3_sitelibdir/azure_mgmt_rdbms*

%files         -n python3-module-azure-mgmt-resource
%doc *.rst sdk/resources/azure-mgmt-resource/README.md
%python3_sitelibdir/azure/mgmt/resource
%python3_sitelibdir/azure_mgmt_resource*

%files         -n python3-module-azure-mgmt-subscription
%doc *.rst sdk/subscription/azure-mgmt-subscription/README.md
%python3_sitelibdir/azure/mgmt/subscription
%python3_sitelibdir/azure_mgmt_subscription*

%changelog
* Tue Aug 15 2023 Pavel Skrylev <majioa@altlinux.org> 20230815-alt1
- Initial build for Sisyphus.
