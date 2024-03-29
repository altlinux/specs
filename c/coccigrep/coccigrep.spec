Name:		coccigrep
Version:	1.20
Release:	alt2
Summary:	Semantic grep for the C language based on coccinelle

Group:		Development/Tools
License:	GPL-3.0
Url:		http://home.regit.org/software/coccigrep/
Vcs:		https://github.com/regit/coccigrep.git
Requires:	spatch
BuildArch:	noarch

Source:		%name-%version.tar

BuildRequires(pre):	rpm-build-python3
BuildRequires:		python3-devel
BuildRequires:		python3-module-setuptools
%{?!_disable_check:
BuildRequires: spatch
}

%description
Coccigrep is a semantic grep for the C and C++ languages based on Coccinelle
(http://coccinelle.lip6.fr). It can be used to find where a given structure is
used in code files. Coccigrep depends on the spatch program which comes with
Coccinelle.

%prep
%setup -q -n %{name}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name "*.py" -o -name "coccigrep" \))

%build
%python3_build_debug
gzip -c coccigrep.1 > coccigrep.1.gz

%install
%python3_install
install -D coccigrep.1.gz %buildroot/%_man1dir/coccigrep.1.gz

%check
cat > test.c <<'EOF'
  struct test { int y; };
  int main() {
    struct test x;
    x.y = 1;
  }
EOF
export PYTHONPATH=./src
./coccigrep -v -t 'struct test' test.c		|| exit 1
./coccigrep -v -t 'struct test' -a 'y' test.c	|| exit 1
./coccigrep -v -t 'struct test' -a 'x' test.c	&& exit 1
./coccigrep -v -t 'test' test.c			&& exit 1

%files
%doc LICENSE README.rst ChangeLog
%_bindir/coccigrep
%_man1dir/*.1*
%python3_sitelibdir/*

%changelog
* Thu Feb 01 2024 Vitaly Chikunov <vt@altlinux.org> 1.20-alt2
- Fix: ALT beekeeper Sisyphus/x86_64 test rebuild failed.

* Tue May 05 2020 Vitaly Chikunov <vt@altlinux.org> 1.20-alt1
- Update to v1.20.

* Tue Apr 07 2020 Vitaly Chikunov <vt@altlinux.org> 1.19-alt1
- Update to v1.19.

* Mon Oct 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.17-alt2
- python2 -> python3

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.17-alt1
- Initial build of coccigrep for ALT.
