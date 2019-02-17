Name: fish
Version: 3.0.1
Release: alt1

Summary: A friendly interactive shell
License: GPLv2+
Group: Shells

URL: http://fishshell.com/

# https://github.com/fish-shell/fish-shell.git
Source: %name-%version.tar

Requires: man
BuildRequires(pre): rpm-build-python3
BuildRequires: libncurses-devel doxygen gcc-c++
BuildRequires: libpcre2-devel >= 10.22

%set_compress_topdir %_mandir

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendliness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%prep
%setup
echo "%version" > version

rm -vrf pcre2-*

# Change the bundled scripts to invoke the python binary directly.
for f in $(find share/tools -type f -name '*.py'); do
    sed -i -e '1{s@^#!.*@#!%{__python3}@}' "$f"
done


%build
%autoreconf
%configure \
	--with-doxygen \
	--without-included-pcre2
%make_build

%install
%makeinstall_std
%find_lang %name

rm -f %buildroot%_datadir/fish/completions/docker.fish

%post
grep -q %_bindir/fish %_sysconfdir/shells ||
	echo %_bindir/fish >>%_sysconfdir/shells

%postun
. shell-quote
if [ "$1" = 0 ]; then
	sed -i "/^$(quote_sed_regexp %_bindir/fish)$/ d" %_sysconfdir/shells
fi

%files -f %name.lang
%_bindir/*
%dir %_sysconfdir/fish
%config %_sysconfdir/fish/config.fish
%_datadir/fish
%doc %_docdir/%name
%_man1dir/*

%changelog
* Sun Feb 17 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- remove completion for docker, fixed file conflict with docker-ce package

* Sun Dec 30 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt2%ubt
- fix find altlinux path /etc/openssh for completions

* Sat Feb 10 2018 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt1%ubt
- 2.7.1

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1%ubt
- 2.7.0

* Tue Oct 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1%ubt
- 2.6.0

* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20140907
- Version 2.1.1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.23.1-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Sun Mar 06 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt2
- Do not compress /usr/share/fish/man/*

* Sat Mar 05 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt1
- Initial build
