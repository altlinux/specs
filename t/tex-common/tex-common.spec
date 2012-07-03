Name: tex-common
Version: 0.2
Release: alt4
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: TeX distribution common files
License: GPL
Group: Publishing
Url: http://git.altlinux.org/people/bga/packages/tex-common.git

BuildArch: noarch

Source0: texhash.trigger

%define lsr %_sysconfdir/texmf %_datadir/texmf %_datadir/texmf/doc %_cachedir/texmf
%define own %lsr %_sysconfdir/tex-fonts.d %_sysconfdir/texmf/fmt.d %_sysconfdir/texmf/language.d %_sysconfdir/texmf/updmap.d
Provides: %(for i in %own; do echo -n "$i "; done)

%description
This package contains files common for all TeX distributions

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

install -m755 %SOURCE0 %buildroot/%_rpmlibdir/texlive-1-texhash.filetrigger

%triggerin -- tetex-core, texlive-base-bin
texhash=%_bindir/texhash
[ -x "$texhash" ] && "$texhash" ||:

%files -f files
%_rpmlibdir/%name-files.req.list
%_rpmlibdir/*.filetrigger

%changelog
* Fri Jun 12 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt4
- Include generated ls-R lists into the package.

* Thu Apr 30 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Fix texlive-1-texhash.filetrigger, so it doesn't fail
  when no tex providers installed.

* Sat Apr 25 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Check if kpsewhich is present before use.

* Thu Apr 23 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Keep texhash filetrigger from texlive.
- Rerun texhash on tetex-core or texlive-base-bin install.

* Wed Mar 25 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt2
- Hold %%_datadir/texmf/doc directory.

* Wed Feb 11 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial build for ALT Linux.

