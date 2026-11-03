Summary: Converts PBM stream to Lexmark 7000, 7200 and 5700 printer language

Name: pbm2l7k
Version: 990321
Release: alt1.qa3

Provides: lexmark700linux = %version

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL
Url: http://bimbo.fjfi.cvut.cz/~paluch/l7kdriver/olddrv.html
Source: %name-%version.tar
Patch0: pnmraw2cmyk-include-dither-header.patch

%description
This is a filter to convert pbmraw data such as produced by ghostscript to
the printer language of Lexmark 7000, 7200 and 5700 printers.  It is meant
to be used by the PostScript Description files of the drivers from the
foomatic package.

%prep
%setup -q -n %name-%version
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
for i in %name; do
install -Dpm755 $i %buildroot/%_bindir/$i
done


%files
%doc README CHANGES lexmark*-filter lexmarkprotocol.txt *.prn *.pbm
%_bindir/*

%changelog
* Tue Nov 03 2026 Vitaly Lipatov <lav@altlinux.ru> 990321-alt1.qa3
- Include the dithering declarations to fix the build.

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 990321-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 990321-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 990321-alt1
- Initial build
