Name: prelude-notify
Version: 0.9.2
Release: alt1.git20120829
Summary: Prelude-Notify is brought to you by CS-SI (http://www.prelude-ids.com)
License: GPLv2
Group: Networking/Other
Url: https://www.prelude-ids.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://prelude-ids.org/git/prelude-notify.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: gcc-c++ libprelude-devel python-devel

%description
Prelude-notify is a desktop oriented application that works as a
monitoring tool that capture events from prelude manager using the
prelude connection pool event checker. Its purpose is to help security
managers and/or administrators to see in real time what's going on in
their network.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc AUTHORS NEWS README
%_bindir/*
%_sysconfdir/%name
%_desktopdir/*
%_datadir/%name
%python_sitelibdir/*

%changelog
* Thu Sep 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20120829
- Initial build for Sisyphus

