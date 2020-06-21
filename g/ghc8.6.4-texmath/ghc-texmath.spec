%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name texmath
%define f_pkg_name texmath
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.12.0.2
Release: alt1
License: GPL-2
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/jgm/texmath
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: Conversion between formats used to represent mathematics.

BuildPreReq: haskell(abi) = %ghc_version
BuildRequires: ghc8.6.4(syb) ghc8.6.4(xml) ghc8.6.4(parsec) ghc8.6.4(containers) ghc8.6.4(pandoc-types) ghc8.6.4(mtl) ghc8.6.4(text)

%description
The texmath library provides functions to read and write TeX math,
presentation MathML, and OMML (Office Math Markup Language, used in
Microsoft Office). Support is also included for converting math formats to
Gnu eqn and to pandoc's native format (allowing conversion, via pandoc, to
a variety of different markup formats). The TeX reader supports basic LaTeX
and AMS extensions, and it can parse and apply LaTeX macros. (See
<http://johnmacfarlane.net/texmath here> for a live demo of bidirectional
conversion between LaTeX and MathML.)

The package also includes several utility modules which may be useful for
anyone looking to manipulate either TeX math or MathML. For example, a copy
of the MathML operator dictionary is included.

Use the @executable@ flag to install a standalone executable, @texmath@,
that by default reads a LaTeX formula from @stdin@ and writes MathML to
@stdout@. With flags all the functionality exposed by 'Text.TeXMath' can be
accessed through this executable. (Use the @--help@ flag for a description
of all functionality)

The @texmath@ executable can also be used as a CGI script, when renamed as
@texmath-cgi@. It will expect query parameters for @from@, @to@, @input@,
and optionally @inline@, and return a JSON object with either @error@ and a
message or @success@ and the converted result.

%prep
%setup
%patch -p1

%build
%hs_configure2 --disable-split-objs
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 0.12.0.2-alt1
- Spec created by cabal2rpm 0.20_10
