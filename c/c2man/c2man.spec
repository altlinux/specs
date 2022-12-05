Name: c2man
#catalog:version:2.0 patchlevel 40
Version: 2.0.40
Release: alt1.1

Summary: C Source Manual Page Extraction Tool
Group: Development/Other
License: GPL
Url: https://github.com/fribidi/c2man

Vcs: https://github.com/fribidi/c2man.git
Source: %name-%version.tar
Patch: c2man-lex.patch

BuildRequires: bison flex

%description
C2man is an automatic documentation tool that extracts comments from C
source code to generate functional interface documentation in the same
format as sections 2 & 3 of the Unix Programmer's Manual. It requires
minimal effort from the programmer by looking for comments in the
usual places near the objects they document, rather than imposing a
rigid function-comment syntax or requiring that the programmer learn
and use a typesetting language. Acceptable documentation can often be
generated from existing code with no modifications.

%prep
%setup
%patch

%build
%ifarch %e2k
# crazy "mkdep" hacks in Configure don't work well for LCC
# make: No rule to make target '-', needed by 'c2man.o'.
touch "./-"
%endif
./Configure -d -e -s \
    -Dcc=gcc \
    -Doptimize="$RPM_OPT_FLAGS" \
    -Dprefix=%_prefix \
    -Dlex=%_bindir/flex \
    -Dyacc="%_bindir/bison -y"
%make_build

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -m755 %name %buildroot%_bindir/
install -m644 %name.1 %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc README CHANGES FAQ


%changelog
* Mon Dec 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.0.40-alt1.1
- fixed build for Elbrus by ilyakurdyukov@

* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.40-alt1
- first build for Sisyphus

