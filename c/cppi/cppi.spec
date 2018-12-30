Name: cppi
Version: 1.18.0.19.0ac4
Release: alt1

Summary: C preprocessor directive indenter
License: GPLv3+
Group: Development/Tools
Url: https://www.gnu.org/software/cppi/

%define srcname %name-%version-%release
# git://git.altlinux.org/gears/c/cppi.git
Source: %srcname.tar

BuildRequires: flex gperf help2man gnulib >= 0.1.2305.95c96

%description
cppi indents the C preprocessor directives to reflect their nesting
and ensure that there is exactly one space character between each #if,
#elif, #define directive and the following token, and write the result
to standard output.  The number of spaces between the `#' and the
following directive must correspond to the level of nesting of that
directive.

%prep
%setup -n %srcname

# Build scripts expect to find the cppi version in this file.
echo -n %version > .tarball-version

# Generate LINGUAS file.
ls po/*.po | sed 's|.*/||; s|\.po$||' > po/LINGUAS

# git, makeinfo, and rsync aren't needed for build.
sed -i '/^\(git\|makeinfo\|rsync\)[[:space:]]/d' bootstrap.conf

%build
./bootstrap --skip-po --gnulib-srcdir=%_datadir/gnulib

%configure \
	--disable-silent-rules \
	--enable-gcc-warnings \
	#
%make_build

%install
%makeinstall_std

%find_lang %name

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_mandir/man?/*
%doc AUTHORS NEWS README THANKS TODO

%changelog
* Sun Dec 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1.18.0.19.0ac4-alt1
- v1.18-19-g0ac456b.
