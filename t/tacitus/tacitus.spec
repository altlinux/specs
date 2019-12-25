%define with_docs 0

Name: tacitus
Version: 0.3
Release: alt1
Group: System/Base
Summary: Set sort-of-actual time on systems without RTC.
License: WTFPL
Source0: %name-%version.tar.xz
# commented out for now; use at your own risk, bwa-ha-ha!
# Conflicts: systemd
Requires: chkconfig coreutils grep
BuildArch: noarch
# most build environments would safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
%summary
NTP daemon would normally do the rest.

%if %with_docs
%package doc
Group: Documentation
Summary: Optional documentation for %name
BuildArch: noarch
%description doc
%summary
%endif


%prep
%setup


%install
rm -rf %buildroot
mkdir -pm755 \
  %buildroot%_initdir \
  %buildroot%_man8dir
install -m755 %name.rc \
  %buildroot%_initdir/%name
install -m644 %name.8 \
  %buildroot%_man8dir/


%post
chkconfig --add %name

%preun
chkconfig --del %name


%clean
rm -rf %buildroot


%files
%_initdir/%name
%_man8dir/%name.*

%if %with_docs
%files doc
%doc *.txt
%endif


%changelog
* Wed Dec 25 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.3-alt1
- one more bash-specific fix

* Wed Oct 02 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.2-alt1
- fix running with damned bash
- enable (though not recommended) use with systemd
- add license file (does anyone really care of them?)

* Tue Sep 24 2019 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- first release for Sisyphus
