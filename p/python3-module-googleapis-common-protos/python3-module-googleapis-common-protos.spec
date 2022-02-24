Name:    python3-module-googleapis-common-protos
Version: 1.55.0
Release: alt1

Summary: Common protobufs used in Google APIs
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/googleapis/python-api-common-protos

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: python-api-common-protos-%version.tar

%description
googleapis-common-protos contains the python classes generated from the common
protos in the googleapis/api-common-protos repository.

%prep
%setup -n python-api-common-protos-%version

%build
%python3_build

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Thu Feb 24 2022 Andrey Cherepanov <cas@altlinux.org> 1.55.0-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.54.0-alt1
- New version.

* Wed May 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.53.0-alt1
- Initial build for Sisyphus
