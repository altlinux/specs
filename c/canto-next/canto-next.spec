Name: canto-next
Version: 0.9.0
Release: alt1.rc1.git20140903.1
Summary: The next generation Canto RSS daemon
License: GPLv2
Group: Networking/News
Url: http://codezen.org/canto-ng/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/themoken/canto-next.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel

%description
This is the RSS backend for Canto clients.

canto-curses is the default client.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%_bindir/*
%_man1dir/*
%python3_sitelibdir/*
%_libexecdir/systemd/user/*

# TODO: SysV init-script

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.rc1.git20140903.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.rc1.git20140903
- Initial build for Sisyphus

