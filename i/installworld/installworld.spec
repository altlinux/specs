%define with_docs 0

Name: installworld
Version: 0.1
Release: alt1
Summary: ALT Linux unattended installation tools
Group: System/Base
License: WTFPL
URL: https://www.altlinux.org/Unattended_install
# git://git.altlinux.org/gears/i/installworld
Source: %name-%version.tar.xz
BuildRoot: %_tmppath/%name-%version-root
BuildArch: noarch
Requires: tcsh rsync

%description
This package contains a collection of scripts for performing
automated system installation, including (but not limited to)
unattended mass deployment.

%if %with_docs
%package doc
Summary: Optional documentation for %name
Group: Documentation
BuildArch: noarch
%description doc
%summary
%endif

%prep
%setup -q -n %name-%version


%install
rm -rf %buildroot
mkdir -p %buildroot%_sbindir %buildroot%_man8dir
install -m 755 \
  scripts/* \
  %buildroot%_sbindir/
install -m 644 \
  man/* \
  %buildroot%_man8dir/


%clean
rm -rf %buildroot %{_builddir}/%{name}-%{version}


%files
%defattr(-,root,root)
%_sbindir/*
%_man8dir/*

%if %with_docs
%files doc
%doc *.txt
%endif

%changelog
* Mon Mar 04 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- first build

