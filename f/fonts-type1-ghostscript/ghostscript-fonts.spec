%define oldname ghostscript-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: Fonts for the Ghostscript PostScript interpreter
Name: fonts-type1-ghostscript
Version: 5.50
Release: alt1_37
# Contacted Kevin Hartig, who agreed to relicense his fonts under the SIL Open Font 
# License. Hershey fonts are under the "Hershey Font License", which is not what Fontmap 
# says (Fontmap is wrong).
License: GPLv2+ and Hershey and MIT and OFL and Public Domain
Group: Publishing
URL: http://www.gnu.org/software/ghostscript/
Source0: gnu-gs-fonts-other-%{version}-nobch.tar.gz
Source1: Kevin_Hartig-Font_License.txt
Source2: SIL-Open-Font-License.txt
# gnu-gs-fonts-other-5.50 contains fonts with a non-free license (bug #690593).
# Therefore we use this script to remove those fonts before shipping
# it.  Download the upstream tarball (from
# http://ftp.gnu.org/gnu/ghostscript/) and invoke this script while in
# the tarball's directory:
# ./generate-tarball.sh 5.50
Source3: generate-tarball.sh
Requires: fontconfig
Requires(post): mkfontdir mkfontscale
Requires(post): fontconfig
Requires(postun): fontconfig
BuildArchitectures: noarch

%define fontdir %{_datadir}/fonts/type1/ghostscript
%define catalogue %{_sysconfdir}/X11/fontpath.d
Source44: import.info

%description
Ghostscript-fonts contains a set of fonts that Ghostscript, a
PostScript interpreter, uses to render text. These fonts are in
addition to the fonts shared by Ghostscript and the X Window System.

%prep
%setup -q -c ghostscript-fonts-%{version}
cp -p %{SOURCE1} %{SOURCE2} .

# Remove Hershey fonts as they cause problems (bug #707007).
find fonts -type f | xargs grep -lw Hershey | xargs rm -f

%build

%install
mkdir -p $RPM_BUILD_ROOT%{fontdir}
cp -p fonts/* $RPM_BUILD_ROOT%{fontdir}

# Touch ghosted files
touch $RPM_BUILD_ROOT%{fontdir}/fonts.{dir,scale}

# Install catalogue symlink
mkdir -p $RPM_BUILD_ROOT%{catalogue}
ln -sf %{fontdir} $RPM_BUILD_ROOT%{catalogue}/default-ghostscript

# touching all ghosts; hack for rpm 4.0.4
for rpm_404_ghost in %{fontdir}/fonts.dir %{fontdir}/fonts.scale
do
    mkdir -p %buildroot`dirname "$rpm_404_ghost"`
    touch %buildroot"$rpm_404_ghost"
done


%post
{
   mkfontscale %{fontdir}
   mkfontdir %{fontdir}
   fc-cache %{fontdir}
} &> /dev/null || :

%postun
{
   if [ "$1" = "0" ]; then
      fc-cache %{fontdir}
   fi
} &> /dev/null || :

%files
%doc Kevin_Hartig-Font_License.txt SIL-Open-Font-License.txt
%{_datadir}/fonts/type1/*
%{catalogue}/default-ghostscript
%ghost %verify(not md5 size mtime) %{fontdir}/fonts.dir
%ghost %verify(not md5 size mtime) %{fontdir}/fonts.scale

%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_37
- update

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_33
- new fc release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_29
- new fc release

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_28
- update to new release by fcimport

* Mon Oct 17 2011 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_27
- update to new release by fcimport

* Wed Aug 31 2011 Igor Vlasenko <viy@altlinux.ru> 5.50-alt1_26
- new release by fcimport

