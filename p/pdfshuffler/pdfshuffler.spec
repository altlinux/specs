Name:           pdfshuffler
Version:        0.7.0
Release:        alt1
Group:          Publishing
Summary:        PDF file merging, rearranging, and splitting

License:        %gpl3only
URL:            http://sourceforge.net/projects/pdfshuffler/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires:  rpm-build-licenses
BuildRequires: /usr/bin/desktop-file-validate

BuildRequires:  python3-module-pkg_resources python3-module-setuptools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext gettext-tools

Requires:       python3-module-PyPDF2
Requires:	libpoppler-gir

%description
PDF-Shuffler is a small python application, which helps the user
to merge or split pdf documents and rotate, crop and rearrange their
pages using an interactive and intuitive graphical interface.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root %{buildroot}


mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,256x256,32x32,48x48,scalable}/apps
cp -ra data/hicolor/* %buildroot%_iconsdir/hicolor/

desktop-file-validate %buildroot%_desktopdir/%{name}.desktop
%find_lang %name

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%_datadir/appdata
cat > $RPM_BUILD_ROOT%_datadir/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/pdfshuffler/feature-requests/34/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">pdfshuffler.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      PDF-Shuffler is a small application, which helps the user to merge or split pdf
      documents and rotate, crop and rearrange their pages using an interactive and
      intuitive graphical interface.
      It is a frontend for python-pyPdf.
    </p>
    <!-- FIXME: Probably needs another paragraph or two -->
  </description>
  <url type="homepage">http://pdfshuffler.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://a.fsdn.com/con/app/proj/pdfshuffler/screenshots/181783.jpg/</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO
%doc --no-dereference COPYING
%_mandir/man*/*.*
%_bindir/%{name}
%_datadir/%{name}/
%_datadir/appdata/%{name}.appdata.xml
%_desktopdir/%{name}.desktop
%_iconsdir/hicolor/*/apps/*
%python3_sitelibdir_noarch/%{name}*.egg-info
%python3_sitelibdir_noarch/%name/

%changelog
* Mon Jan 30 2023 Artyom Bystrov <arbars@altlinux.org> 0.7.0-alt1
- initial commit for Sisyphus

* Tue Apr 12 2022 Anton Shevtsov <shevtsov.anton@gmail.co> 0.7.0-alt1
- Switching to Python 3
- Port to Gtk+3
- Switching to PyPDF2 

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_17
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_16
- update to new release by fcimport

* Sun Sep 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_15
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_14
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_11
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_10
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_9
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_8
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_7
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_5
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_4
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_0.4.20120302svn64
- initial fc import

