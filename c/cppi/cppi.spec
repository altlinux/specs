Name: cppi
Version: 1.18.0.36.4f20
Release: alt1

Summary: C preprocessor directive indenter
License: GPLv3+
Group: Development/Tools
Url: https://www.gnu.org/software/cppi/

%define srcname %name-%version-%release
# git://git.altlinux.org/gears/c/cppi.git
Source: %srcname.tar

BuildRequires: flex gperf help2man gnulib >= 0.1.4170.b0728

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

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_mandir/man?/*
%doc AUTHORS NEWS README THANKS TODO

%changelog
* Sun Apr 30 2023 Dmitry V. Levin <ldv@altlinux.org> 1.18.0.36.4f20-alt1
- cppi: v1.18-27-g040518f -> v1.18-36-g4f206f0.

* Mon Apr 12 2021 Dmitry V. Levin <ldv@altlinux.org> 1.18.0.27.0405-alt1
- cppi: v1.18-19-g0ac456b -> v1.18-27-g040518f.
- gnulib BR: v0.1-2305-g95c96b6dd-> v0.1-4170-gb07286e46.
- Updated translations from translationproject.org.

* Sun Dec 30 2018 Dmitry V. Levin <ldv@altlinux.org> 1.18.0.19.0ac4-alt1
- v1.18-19-g0ac456b.
