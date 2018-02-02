%define _unpackaged_files_terminate_build 1
%define oname cubicweb-sioc
Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: Specific views for SIOC (Semantically-Interlinked Online Communities)
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-sioc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/ec/86/5ebbc599acbcf37525a51308f9ee4e3436bd9280423961f8f9bb23991dc5/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb
BuildPreReq: python-module-markdown

Requires: cubicweb

%description
Specific views for SIOC (Semantically-Interlinked Online Communities).

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

