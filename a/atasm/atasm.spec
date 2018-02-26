# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           atasm
Version:        1.07d
Release:        alt2_3
Summary:        6502 cross-assembler

Group:          Development/Tools
License:        GPLv2+
URL:            http://atari.miribilist.com/atasm/
Source0:        http://atari.miribilist.com/atasm/%{name}107d.zip
#Source0:        http://downloads.sourceforge.net/%{name}/%{name}106.zip

BuildRequires:  zlib-devel
Source44: import.info


%description
ATasm is a 6502 command-line cross-assembler that is compatible with the
original Mac/65 macroassembler released by OSS software.  Code
development can now be performed using "modern" editors and compiles
with lightning speed.


%prep
%setup -q -n %{name}107


%build
pushd src
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -DZLIB_CAPABLE -DUNIX"
sed -e 's|%%DOCDIR%%|%{_docdir}/%{name}-%{version}|g' %{name}.1.in > %{name}.1
popd


%install

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1

pushd src
install -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install -p -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
popd


%check
pushd tests
make test
popd


%files
%doc LICENSE VERSION.TXT docs/atasm.blurb docs/atasm.pdf examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.07d-alt1_2
- initial release by fcimport

