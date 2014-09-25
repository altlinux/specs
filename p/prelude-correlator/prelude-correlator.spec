Name: prelude-correlator
Version: 1.2.6
Release: alt1.rc2.git20140923
Summary: The Prelude-Correlator
License: GPLv2
Group: Networking/Other
Url: http://www.prelude-ids.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://prelude-ids.org/git/prelude-correlator.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-c++ libprelude-devel python-devel
BuildPreReq: python-module-setuptools

%description
Prelude-Correlator allows conducting multistream correlations thanks to
a powerful programming language for writing correlation rules. With any
type of alert able to be correlated, event analysis becomes simpler,
quicker and more incisive.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS HACKING.README NEWS README docs/*
%_bindir/*
%_sysconfdir/%name
%python_sitelibdir/*
%_localstatedir/*

%changelog
* Thu Sep 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.rc2.git20140923
- Initial build for Sisyphus

