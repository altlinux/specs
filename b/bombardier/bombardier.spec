Name: bombardier
Version:  0.8.2.2
Release:  alt2_12
Summary: The GNU Bombing utility

Group: Games/Other
License: GPLv2+        
URL: http://packages.debian.org/stable/source/bombardier
Source0: http://ftp.debian.org/debian/pool/main/b/bombardier/bombardier_0.8.2.2.tar.gz
Source1: bombardier.desktop
Source2: bombardier-logo.png
Patch0: bombardier-height.patch
Patch1: bombardier-rpm_opt_flags.patch
Patch2: bombardier-hof-open-mode.patch
BuildRequires: libncurses-devel desktop-file-utils
Requires: icon-theme-hicolor
Source44: import.info


%description
Fly an ncurses plane over an ncurses city, and try to level the buildings.

%prep


%setup -qn bombardier-0.8.2

%patch0 -p0
%patch1 -p0
%patch2 -p0

# link with --as-needed
sed -i -e 's,$(LDFLAGS) -o $@ $(OBJS),-o $@ $(OBJS) $(LDFLAGS),' Makefile

%build
make CFLAGS="$RPM_OPT_FLAGS"


%install
install -pD -m 755 bombardier %{buildroot}%{_bindir}/bombardier
install -pD -m 644 bombardier.6 %{buildroot}%{_mandir}/man6/bombardier.6

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install             \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

%files
%{_bindir}/bombardier
%doc README DEDICATION COPYING VERSION
%{_datadir}/applications/bombardier.desktop
%{_datadir}/icons/hicolor/32x32/apps/bombardier-logo.png
%{_mandir}/man6/bombardier.6.*


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt1_12
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.2.2-alt1_11
- initial release by fcimport

