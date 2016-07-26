# BEGIN SourceDeps(oneline):
BuildRequires: perl(Digest/MD5.pm) perl(Digest/SHA1.pm) perl(Locale/gettext.pm) perl(Text/Tabs.pm) perl(Time/Local.pm)
# END SourceDeps(oneline)
Name:           dc3dd
Version:        7.1.614
Release:        alt2_10
Summary:        Patched version of GNU dd for use in computer forensics

Group:          Editors
License:        GPLv2+ and GPLv3+
URL:            http://dc3dd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dc3dd/%{name}-%{version}.tar.gz

#Fixing build error: automatic de-ANSI-fication support has been removed
#Removing the check for AM_C_PROTOTYPES
Patch0:         dc3dd-automake.patch

BuildRequires: gettext gettext-tools gettext-tools-python
BuildRequires: gettext-tools libasprintf-devel
BuildRequires:  m4, readline-devel, autoconf-common, automake-common
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
%patch0 -p 1 -b .automake

### Release dc3dd-7.1.614.tar.gz removed the need for this
#
#for file in README Sample_Commands.txt Options_Reference.txt; 
#do
#    sed 's|\r||' $file > $file.tmp
#    touch -r $file $file.tmp
#    mv -f $file.tmp $file
#done
#rm po/*.gmo

%build
autoreconf -vif #BZ925238 - support aarch64
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING ChangeLog README README.coreutils THANKS THANKS-to-translators TODO Sample_Commands.txt NEWS Options_Reference.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%changelog
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

