%define oname DistroDbMaker

%def_without python3

Name: python-module-%oname
Version: 0.004
Release: alt1
Summary: DistroDb Maker tools
License: LGPL2+
Group: Development/Python
Url: https://www.altlinux.org/Packaging_Automation/DistroDb

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Conflicts: distrodb-utils < 0.21
Requires: python-module-rpm python-module-backports.lzma
#py_provides %oname

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: DistroDb Maker tools
Group: Development/Python3
#py3_provides %oname

%description -n python3-module-%oname
%summary
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%_bindir/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Sun Feb 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- mageia texlive support

* Fri Feb 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- alt support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- xz list support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- Initial build for Sisyphus
