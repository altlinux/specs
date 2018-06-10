Name:		coccigrep
Version:	1.17
Release:	alt1
Summary:	Semantic grep for the C language based on coccinelle

Group:		Development/Tools
License:	GPLv3
Url:		http://home.regit.org/software/coccigrep/
Requires:	spatch
BuildArch:	noarch

Source:		%name-%version.tar

BuildRequires:	rpm-build-python
BuildRequires:	python-devel
BuildRequires:	python-module-setuptools
%{?!_without_check:%{?!_disable_check:BuildRequires: spatch}}

%description
Coccigrep is a semantic grep for the C language based on coccinelle. It can be
used to find where a given structure is used in code files. coccigrep depends
on the spatch program which comes with coccinelle.

%prep
%setup -q -n %{name}-%{version}

%build
%python_build_debug
gzip -c coccigrep.1 > coccigrep.1.gz

%install
%python_install
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
./coccigrep -t 'struct test' test.c		|| exit 1
./coccigrep -t 'struct test' -a 'y' test.c	|| exit 1
./coccigrep -t 'struct test' -a 'x' test.c	&& exit 1
./coccigrep -t 'test' test.c			&& exit 1

%files
%doc LICENSE README.rst ChangeLog
%_bindir/coccigrep
%_man1dir/*.1*
%python_sitelibdir/*

%changelog
* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.17-alt1
- Initial build of coccigrep for ALT.
