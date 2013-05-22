BuildRequires(pre): rpm-build-python3
%define oldname python-module-crank
%define oname crank
Name: python3-module-%oname
Version: 0.6.4
Release: alt1
Summary: Generalization of dispatch mechanism for use across frameworks
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/crank/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oldname-%version.tar
BuildArch: noarch

BuildPreReq: python3-devel python3-module-distribute

%description
Generalization of dispatch mechanism for use across frameworks.

%prep
%setup -n %{oldname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Thu May 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- python3 copycat test run

