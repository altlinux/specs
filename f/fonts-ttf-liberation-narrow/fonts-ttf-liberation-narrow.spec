%define oldname liberation-fonts
%global priority  59
%global fontname liberation-narrow
%global fontconf %{priority}-%{fontname}

Name:             fonts-ttf-%fontname
Summary:          Sans-serif Narrow fonts to replace commonly used Microsoft Arial Narrow

Version:          1.07.4
Release:          alt1
# The license of the Liberation Fonts is a EULA that contains GPLv2 and two
# exceptions:
# The first exception is the standard FSF font exception.
# The second exception is an anti-lockdown clause somewhat like the one in
# GPLv3. This license is Free, but GPLv2 and GPLv3 incompatible.
License:          Liberation
Group:            System/Fonts/True type
URL:              http://fedorahosted.org/liberation-fonts/
Source0:          https://fedorahosted.org/releases/l/i/liberation-fonts/%{oldname}-%{version}.tar.gz
Source5:          %{oldname}-narrow.conf
BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13 xorg-x11-font-utils
BuildRequires:    fontforge
BuildRequires: rpm-build-fonts
Source44: import.info

Conflicts: fonts-ttf-liberation < 1.07

%description
The Liberation Fonts are intended to be replacements for the three most \
commonly used fonts on Microsoft systems: Times New Roman, Arial, and Courier \
New.

This is Sans-Serif Narrow TrueType fonts that replaced commonly used Microsoft \
Arial Narrow.

%prep
%setup -q -n %{oldname}-%{version}

%build
make %{?_smp_mflags} 
mv liberation-fonts-ttf-%{version}/* .

%install
%ttf_fonts_install %fontname

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

  ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

%files -f %fontname.files
%doc License.txt README AUTHORS ChangeLog
%{_fontconfig_templatedir}/*-%{fontname}.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}.conf

%changelog
* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.07.4-alt1
- as of 2.00 liberation-narrow is not included in liberation fonts 
  due to license incompatibilities. Use release 1.07.4

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.06.0.20100721-alt1
- build new upstream release

* Wed Dec 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt2
- add fonts-ttf-core provides (ALT bug #22589)

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt1
- new version 1.0.4
- removed License.txt as already included in sources

* Wed May 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt1
- new version (fix altbug #15355)
- update to Caius Chance <cchance@redhat.com> version of the project
  + Resolves: rhbz#251890 (Exchanged and incomplete glyphs.)
  + Resolves: rhbz#240525 (Alignment mismatch of dot accents.)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sun May 13 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
