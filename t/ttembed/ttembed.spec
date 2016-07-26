Group: Development/Tools
Name:       ttembed
Version:    1.1
Release:    alt1_5
Summary:    Remove embedding limitations from TrueType fonts
License:    Public Domain
URL:        https://github.com/hisdeedsaredust/ttembed
Source0:    https://github.com/hisdeedsaredust/ttembed/archive/v%{version}.tar.gz
Source44: import.info

%description
Remove embedding limitations from TrueType fonts, by setting the fsType field
in the OS/2 table to zero. That's it; this program is a one-trick pony.

%prep
%setup -q

%build
export CFLAGS="$CFLAGS %{optflags}"
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1/
install -p -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/%{name}
%{_mandir}/man1/*
%doc LICENSE README.md

%check
# smoke test - fail on not font file
echo 'not a font' > test
if [[ "$(./ttembed test 2>&1)" != "test: Not TTF/OTF" ]] ; then
    echo "TEST FAIL: not a font input test" 1>&2
    exit 1
fi
rm test

%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2
- converted for ALT Linux by srpmconvert tools

