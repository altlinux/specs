Group: System/Fonts/X11 bitmap
%define oldname iso8859-2-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname iso8859-2

%global __mkfontdir umask 133;mkfontdir
%global catalogue  %{_sysconfdir}/X11/fontpath.d

Name:           fonts-bitmap-iso8859-2
Version:        1.0
Release:        alt2_36
Summary:        Central European language fonts for the X Window System
License:        MIT
# Upstream url http://www.biz.net.pl/images/ISO8859-2-bdf.tar.gz is dead now.
Source:         ISO8859-2-bdf.tar.gz

Patch0:         XFree86-ISO8859-2-1.0-redhat.patch
BuildArch:      noarch
Buildrequires:  bdftopcf mkfontdir mkfontscale xorg-font-utils
BuildRequires:  fontpackages-devel
Requires:       mkfontdir
Source44: import.info
Url: http://xorg.freedesktop.org
 
%description
If you use the X Window System and you want to display Central
European fonts, you should install this package.


%package -n fonts-bitmap-iso8859-2-common
Group: System/Fonts/X11 bitmap
Summary:        Common files of %{oldname}

%description -n fonts-bitmap-iso8859-2-common
Common files of %{oldname}.


%package -n fonts-bitmap-iso8859-2-misc
Group: System/Fonts/X11 bitmap
Summary:        A set of misc Central European language fonts for X
Obsoletes:      fonts-ISO8859-2 < 1.0-23
Provides:       fonts-ISO8859-2 = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n fonts-bitmap-iso8859-2-misc
This package contains a set of Central European fonts, in
compliance with the ISO8859-2 standard.


%package -n fonts-bitmap-iso8859-2-75dpi
Group: System/Fonts/X11 bitmap
Summary:        A set of 75dpi Central European language fonts for X
Obsoletes:      fonts-ISO8859-2-75dpi < 1.0-23
Provides:       fonts-ISO8859-2-75dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n fonts-bitmap-iso8859-2-75dpi
This package contains a set of Central European language fonts in 75 dpi
resolution for the X Window System. 


%package -n fonts-bitmap-iso8859-2-100dpi
Group: System/Fonts/X11 bitmap
Summary:        A set of 100dpi Central European language fonts for X
Obsoletes:      fonts-ISO8859-2-100dpi < 1.0-23
Provides:       fonts-ISO8859-2-100dpi = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}
Requires:       mkfontdir

%description -n fonts-bitmap-iso8859-2-100dpi
This package includes Central European (ISO8859-2) fonts, in 100 dpi
resolution, for the X Window System.


%prep
%setup -n %{oldname}-%{version} -c -q
chmod 644 RELEASE_NOTES.TXT
sed -i "/\--0/d" 100dpi/fonts.alias
sed -i "/\--0/d" 75dpi/fonts.alias

%patch0 -p1 -b .redhat

%build
make all

%install
make install PREFIX=$RPM_BUILD_ROOT \
           FONTDIR=$RPM_BUILD_ROOT%{_fontdir}

# Install catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{_fontdir}/misc $RPM_BUILD_ROOT%{catalogue}/%{fontname}-misc-fonts
ln -sf %{_fontdir}/75dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-75dpi-fonts
ln -sf %{_fontdir}/100dpi $RPM_BUILD_ROOT%{catalogue}/%{fontname}-100dpi-fonts

%post -n fonts-bitmap-iso8859-2-misc
{
    %__mkfontdir %{_fontdir}/misc
} &> /dev/null || :

%post -n fonts-bitmap-iso8859-2-75dpi
{
    %__mkfontdir %{_fontdir}/75dpi
} &> /dev/null || :

%post -n fonts-bitmap-iso8859-2-100dpi
{
    %__mkfontdir %{_fontdir}/100dpi
} &> /dev/null || :


%files -n fonts-bitmap-iso8859-2-misc
%doc
%dir %{_fontdir}/misc
%{_fontdir}/misc/*.gz
%verify(not md5 size mtime) %{_fontdir}/misc/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/misc/fonts.dir
%{catalogue}/%{fontname}-misc-fonts

%files -n fonts-bitmap-iso8859-2-75dpi
%doc
%dir %{_fontdir}/75dpi
%{_fontdir}/75dpi/*.gz
%verify(not md5 size mtime) %{_fontdir}/75dpi/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/75dpi/fonts.dir
%{catalogue}/%{fontname}-75dpi-fonts

%files -n fonts-bitmap-iso8859-2-100dpi
%doc
%dir %{_fontdir}/100dpi
%{_fontdir}/100dpi/*.gz
%verify(not md5 size mtime) %{_fontdir}/100dpi/fonts.alias
%verify(not md5 size mtime) %{_fontdir}/100dpi/fonts.dir
%{catalogue}/%{fontname}-100dpi-fonts

%files -n fonts-bitmap-iso8859-2-common
%doc *.TXT
%dir %{_fontdir}

%changelog
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_36
- added URL

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_34
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_30
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_28
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_27
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_26
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_26
- update to new release by fcimport

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_25
- new release by fcimport

