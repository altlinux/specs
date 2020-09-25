Summary: reports bugs in the Debian distribution
Name: reportbug-debian
# python3 -c "import reportbug; print(reportbug.VERSION_NUMBER)"
Version: 7.7.0.1
Release: alt0.2
Packager: Igor Vlasenko <viy@altlinux.ru>
License: GPLv2+
Group: Development/Tools
URL: https://salsa.debian.org/reportbug-team/reportbug
Source: %name-%version.tar
Patch: reportbug.7.7.0-no-query-local-system.patch
BuildArch: noarch
Requires: python3-module-%name = %EVR
BuildRequires: python3-devel rpm-build-python3

%description
reportbug is a tool designed to make the reporting of bugs in Debian
and derived distributions relatively painless.  Its features include:
  * Integration with many mail user agents.
  * Access to outstanding bug reports to make it easier to identify
    whether problems have already been reported.
  * Automatic checking for newer versions of packages.
  * Optional automatic verification of integrity of packages via debsums.
  * Support for following-up on outstanding reports.
  * Optional PGP/GnuPG integration.

Bug reporting in Debian relies on email; reportbug can use a local
mail transport agent (like exim or sendmail), submit directly through
an external mail server, or pass messages to an installed mail user
agent (e.g., mutt) for submission.

This package also includes the "querybts" script for browsing the
Debian bug tracking system.

%package -n python3-module-%name
Group: Development/Tools
Summary: Python modules for interacting with bug tracking systems
#Requires: python3-module-debian python3-module-debianbts python3-module-requests

%description -n python3-module-%name
reportbug is a tool designed to make the reporting of bugs in Debian
and derived distributions relatively painless.

This package includes Python modules which may be reusable by other
tools that want to interact with the Debian bug tracking system.

To actually report a bug, install the reportbug package.

%package gtk
Group: Development/Tools
Summary: reports bugs in the Debian distribution (GTK+ UI)
Requires: %name = %EVR
#python3-gi python3-gi-cairo python3-gtkspellcheck
# gir1.2-gtk-3.0 gir1.2-vte-2.91 gir1.2-gtksource-3.0
Requires: libgtk+3-gir-devel libvte3-gir-devel libgtksourceview3-gir-devel

%description gtk
reportbug is a tool designed to make the reporting of bugs in Debian
and derived distributions relatively painless.  Its features include:

 * Integration with many mail user agents.
 * Access to outstanding bug reports to make it easier to identify
   whether problems have already been reported.
 * Automatic checking for newer versions of packages.
 * Optional automatic verification of integrity of packages via debsums.
 * Support for following-up on outstanding reports.
 * Optional PGP/GnuPG integration.

Bug reporting in Debian relies on email; reportbug can use a local
mail transport agent (like exim or sendmail), submit directly through
an external mail server, or pass messages to an installed mail user
agent (e.g., mutt) for submission.

This package contains a desktop file and icon, and has dependencies
to enable the GTK+ UI mode of reportbug to work.

%prep
%setup -q
%patch -p1

%build
%python3_build

%install
%python3_install

install -m644 -D conf/reportbug.conf %buildroot%_sysconfdir/reportbug.conf
install -m644 -D share/debian-swirl.svg %buildroot%_iconsdir/hicolor/scalable/places/debian-swirl.svg
install -m644 -D debian/reportbug.desktop %buildroot%_desktopdir/reportbug.desktop

mkdir -p %buildroot%_man1dir %buildroot%_man5dir
install -m644 man/*.1 %buildroot%_man1dir/
install -m644 man/*.5 %buildroot%_man5dir/

sed -i s,Exec=reportbug,Exec=reportbug-debian, %buildroot%_desktopdir/reportbug.desktop
mv %buildroot%_desktopdir/reportbug{,-debian}.desktop
mv %buildroot%_bindir/reportbug{,-debian}
mv %buildroot%_man1dir/reportbug{,-debian}.1
mv %buildroot%_bindir/querybts{,-debian}
mv %buildroot%_man1dir/querybts{,-debian}.1


%files
%doc doc/README.developers
%doc doc/README.Users
%doc doc/README.source
%doc doc/HowToReportGoodBugs.txt
%_sysconfdir/reportbug.conf
%_bindir/*-debian
%_man1dir/*-debian.1*
%_man5dir/*
%dir %_datadir/bug
%_datadir/bug/reportbug
%_datadir/reportbug

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%files gtk
%_iconsdir/hicolor/scalable/places/debian-swirl.svg
%_desktopdir/%name.desktop

%changelog
* Fri Sep 25 2020 Igor Vlasenko <viy@altlinux.ru> 7.7.0.1-alt0.2
- new version

