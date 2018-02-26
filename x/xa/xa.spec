Name:           xa
Version:        2.3.5
Release:        alt2_6
Summary:        6502/65816 cross-assembler

Group:          Development/Tools
License:        GPLv2+
URL:            http://www.floodgap.com/retrotech/xa/
Source0:        http://www.floodgap.com/retrotech/%{name}/dists/%{name}-%{version}.tar.gz
# fix conflict with recent glibc, reported in private email
Patch0:         %{name}-2.3.5-getline.patch
# update the build system, reported in private email
Patch1:         %{name}-2.3.5-make.patch
Source44: import.info


%description
xa is a high-speed, two-pass portable cross-assembler. It understands
mnemonics and generates code for NMOS 6502s (such as 6502A, 6504, 6507,
6510, 7501, 8500, 8501, 8502 ...), CMOS 6502s (65C02 and Rockwell R65C02)
and the 65816.

Key amongst its features:

    * C-like preprocessor (and understands cpp for additional feature support)
    * rich expression syntax and pseudo-op vocabulary
    * multiple character sets
    * binary linking
    * supports o65 relocatable objects with a full linker and relocation suite, 
      as well as "bare" plain binary object files
    * block structure for label scoping 


%prep
%setup -q
%patch0 -p1 -b .getline
%patch1 -p1 -b .make

# fix encoding
for f in ChangeLog
do
    iconv -f ISO-8859-1 -t UTF-8 < $f > $f.new
    touch -r $f $f.new
    mv $f.new $f
done


%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"


%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} INSTALL="install -p"


%files
%doc COPYING ChangeLog README.1st doc/xa.txt
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_6
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_5
- initial release by fcimport

