%define  oname ejson

Name:    python3-module-%oname
Version: 0.1.5
Release: alt2

Summary: Extensible JSON serializers and deserializers

License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/Yipit/ejson

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python3

BuildArch: noarch

Source:  %oname-%version.tar


%description
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- Porting on Python3.

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
