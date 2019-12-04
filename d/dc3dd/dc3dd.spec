Group: Editors
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           dc3dd
Version:        7.2.646
Release:        alt1_9
Summary:        Patched version of GNU dd for use in computer forensics

License:        GPLv3+
URL:            http://sourceforge.net/projects/dc3dd/
Source0:        http://downloads.sourceforge.net/dc3dd/%{name}-%{version}.tar

#Fixing build error: automatic de-ANSI-fication support has been removed
#Removing the check for AM_C_PROTOTYPES
Patch1:         dc3dd-01_automake.patch

# Original Archlinux patch to fix build with recent libtools version
# Author: mschlenker
Patch2:         dc3dd-02_fix-FTBFS-with-glibc-2.28.patch


BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gettext gettext-tools
BuildRequires:  gettext-tools libasprintf-devel
BuildRequires:  gnulib
BuildRequires:  perl(Locale/gettext.pm)
BuildRequires:  p7zip-standalone p7zip
BuildRequires:  m4, readline-devel, autoconf, automake
Source44: import.info

%description
dc3dd is a patched version of GNU dd to include a number of features useful
for computer forensics. Many of these features were inspired by dcfldd, but
were rewritten for dc3dd.

* Pattern writes. The program can write a single hexadecimal value or a
    text string to the output device for wiping purposes.
* Piecewise and overall hashing with multiple algorithms and variable 
    size windows. Supports MD5, SHA-1, SHA-256, and SHA-512. Hashes can be 
    computed before or after conversions are made.
* Progress meter with automatic input/output file size probing
* Combined log for hashes and errors
* Error grouping. Produces one error message for identical sequential 
    errors
* Verify mode. Able to repeat any transformations done to the input 
    file and compare it to an output.
* Ability to split the output into chunks with numerical or alphabetic 
    extensions


%prep
%setup -q
%patch1 -p1
%patch2 -p1


#Missing x flag in version 7.2.646 makes the build fail
chmod +x build-aux/git-version-gen configure

# ChangeLog having wrong ends of lines
sed -i -e 's|\r||g' ChangeLog


%build
autoreconf -vif #BZ925238 - support aarch64
# TODO check the --enable-hdparm option
%configure 
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%files -f %{name}.lang
%doc --no-dereference COPYING
%doc ABOUT-NLS AUTHORS ChangeLog README README.coreutils THANKS THANKS-to-translators TODO Sample_Commands.txt NEWS Options_Reference.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 7.2.646-alt1_9
- fixed build

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 7.2.646-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 7.2.641-alt1_2
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt2_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt2_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt2_7
- update to new release by fcimport

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt2_6
- moved to Sisyphus by mike@ request

* Thu Jan 23 2014 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt1_6
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt1_3
- update to new release by fcimport

* Fri Dec 14 2012 Igor Vlasenko <viy@altlinux.ru> 7.1.614-alt1_2
- converted for ALT Linux by srpmconvert tools

