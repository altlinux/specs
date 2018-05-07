Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /perl(www.pl/d
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Enable ImageMagick for converting images other than EPS and XBM
%if 0%{?rhel}
%bcond_with html2ps_enables_ImageMagick
%else
%bcond_without html2ps_enables_ImageMagick
%endif
# Otherwise handle JPEG images with djpeg
%bcond_without html2ps_enables_djpeg
# Otherwise handle images with netpbm
%bcond_without html2ps_enables_netpbm

%define my_subversion b7
Name:           html2ps
Version:        1.0
Release:        alt2_0.29.%{my_subversion}
Summary:        HTML to PostScript converter
License:        GPLv2+
URL:            http://user.it.uu.se/~jan/%{name}.html
Source0:        http://user.it.uu.se/~jan/%{name}-1.0%{my_subversion}.tar.gz
Source1:        xhtml2ps.desktop
Patch0:         http://ftp.de.debian.org/debian/pool/main/h/%{name}/%{name}_1.0b5-5.diff.gz
# use xdg-open in xhtml2ps
Patch1:         %{name}-1.0b5-xdg-open.patch
# patch config file from debian to use dvips, avoid using weblint 
# don't set letter as default page type, paperconf will set the default
Patch2:         %{name}-1.0b5-config.patch
# Remove deprecated variable, bug #822117
Patch3:         %{name}-1.0b7-Remove-deprecated-variable.patch
# Fix Perl 5.22 warnings, bug #1404275
Patch4:         html2ps-1.0b7-Fix-perl-5.22-warnings.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  glibc-locales glibc-timezones glibc-utils iconv
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  sed
Requires:       ghostscript-utils ghostscript
# Depend on paperconf directly (instead of libpaper package) for rpmlint sake
Requires:       %{_bindir}/paperconf
Requires:       perl(HTTP/Cookies.pm)
Requires:       perl(HTTP/Request.pm)
Requires:       perl(LWP/UserAgent.pm)
Requires:       tex(dvips)
Requires:       tex(tex)

# Remove ImageMagick dependency if the feature is disabled
%if %{without html2ps_enables_ImageMagick}

%if %{with html2ps_enables_djpeg}
# libjpeg-turbo-utils for djpeg
Requires:       libjpeg-utils
%endif
%if %{with html2ps_enables_netpbm}
Requires:       netpbm
%endif
%endif
Source44: import.info
%filter_from_requires /^perl(Image.Magick.pm)/d

%description
An HTML to PostScript converter written in Perl.
* Many possibilities to control the appearance. 
* Support for processing multiple documents.
* A table of contents can be generated.
* Configurable page headers/footers.
* Automatic hyphenation and text justification can be selected. 


%package -n xhtml2ps
Group: Publishing
Summary:     GUI front-end for html2ps
Requires:    html2ps = %{version}-%{release}
Requires:    xdg-utils

%description -n xhtml2ps
X-html2ps is freely-available GUI front-end for html2ps, a HTML-to-PostScript
converter.


%prep
%setup -q -n %{name}-1.0%{my_subversion}
%patch0 -p1
%patch1 -p1 -b .xdg-open
%patch2 -p1 -b .config
%patch3 -p1 -b .deprecated

# convert README to utf8
iconv -f latin1 -t utf8 < README > README.utf8
touch -c -r README README.utf8
mv README.utf8 README

patch -p1 < debian/patches/01_manpages.dpatch
# 03_html2ps.dpatch is against 1.0b5, adjust it to 1.0b6
< debian/patches/03_html2ps.dpatch sed -e 's|/opt/misc/|/it/sw/share/www/|' | \
    patch -p1

%patch4 -p1

%build
# Change default configuration
sed -i \
    -e 's/ImageMagick: [01]/ImageMagick: %{with html2ps_enables_ImageMagick}/' \
    -e 's/PerlMagick: [01]/PerlMagick: %{with html2ps_enables_ImageMagick}/' \
    debian/config/html2psrc
%if %{without html2ps_enables_ImageMagick}
sed -i \
    -e '/package {/ a \ \ \ \ djpeg: %{with html2ps_enables_djpeg};' \
    -e '/package {/ a \ \ \ \ netpbm: %{with html2ps_enables_netpbm};' \
    debian/config/html2psrc
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man{1,5}

sed -e 's;/etc/html2psrc;%{_sysconfdir}/html2psrc;' \
    -e 's;/usr/share/doc/html2ps;%{_docdir}/%{name};' \
        html2ps > $RPM_BUILD_ROOT%{_bindir}/html2ps
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/html2ps
install -p -m0644 html2ps.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0644 html2psrc.5 $RPM_BUILD_ROOT%{_mandir}/man5
sed -e 's;/usr/bin;%{_bindir};' \
    -e 's;/usr/share/texmf-texlive;%{_datadir}/texmf;' \
    debian/config/html2psrc > $RPM_BUILD_ROOT%{_sysconfdir}/html2psrc

install -m0755 -p contrib/xhtml2ps/xhtml2ps $RPM_BUILD_ROOT%{_bindir}
desktop-file-install \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE1}


%files
%doc --no-dereference COPYING
%doc README sample html2ps.html
%config(noreplace) %{_sysconfdir}/html2psrc
%{_bindir}/html2ps
%{_mandir}/man1/html2ps.1*
%{_mandir}/man5/html2psrc.5*

%files -n xhtml2ps
%doc --no-dereference contrib/xhtml2ps/LICENSE
%doc contrib/xhtml2ps/README
%{_bindir}/xhtml2ps
%{_datadir}/applications/*xhtml2ps.desktop

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.29.b7
- update to new release by fcimport

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.27.b7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.24.b7
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.22.b7
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.20.b7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.18.b7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.17.b7
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.16.b7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.15.b7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.14.b7
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.13.b7
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.12.b7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.11.b7
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.10.b7
- update to new release by fcimport

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.9.b7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.8.b7
- rebuild to get rid of #27020

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.8.b7
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.7.b7
- initial release by fcimport

