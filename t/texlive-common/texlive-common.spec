Name: texlive-common
Version: 0.1
Release: alt3
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: TeXLive distribution common files
License: GPL
Group: Publishing
Url: http://git.altlinux.org/people/bga/packages/texlive-common.git

BuildArch: noarch

%define lsr %_datadir/texmf-texlive
%define own %lsr %_datadir/texmf-texlive/doc
Provides: %(for i in %own; do echo -n "$i "; done)

%description
This package contains files common for all TeXLive parts

%install
mkdir -p %buildroot%_rpmlibdir
echo '# %name dirlist for %_rpmlibdir/files.req' \
	>%buildroot%_rpmlibdir/%name-files.req.list
for i in %own; do
	mkdir -p %buildroot$i
	printf '%%s\t%%s\n' "$i" %name \
		>>%buildroot%_rpmlibdir/%name-files.req.list
	echo "%%dir $i"
done >files
for i in %lsr; do
	mkdir -p %buildroot$i
	touch "%buildroot$i/ls-R"
	echo "%%ghost $i/ls-R"
done >>files

%files -f files
%_rpmlibdir/%name-files.req.list

%changelog
* Fri Jun 12 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt3
- Include generated ls-R lists into the package.

* Wed Mar 25 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- Hold %%_datadir/texmf-texlive/doc directory.

* Wed Feb 11 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux.
