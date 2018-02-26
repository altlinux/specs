Summary: Converts PBM stream to Lexmark 7000, 7200 and 5700 printer language

Name: pbm2l7k
Version: 990321
Release: alt1

Provides: lexmark700linux = %version

Packager: Stanislav Ievlev <inger@altlinux.org>

Group: Publishing
License: GPL

Source: %name-%version.tar

%description
This is a filter to convert pbmraw data such as produced by ghostscript to
the printer language of Lexmark 7000, 7200 and 5700 printers.  It is meant
to be used by the PostScript Description files of the drivers from the
foomatic package.

%prep
%setup -q -n %name-%version

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
for i in %name; do
%__install -Dpm755 $i %buildroot/%_bindir/$i
done


%files
%doc README CHANGES lexmark*-filter lexmarkprotocol.txt *.prn *.pbm
%_bindir/*

%changelog
* Tue Nov 06 2007 Stanislav Ievlev <inger@altlinux.org> 990321-alt1
- Initial build
