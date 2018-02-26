# NOTE:
# - this software use own GooeyPy with own modifications and new features
#   so it can't use GooeyPy from package (python-GooeyPy.spec)
Name: snowballz
Version: 0.9.5.1

Summary: The fun, free snowballing computer game

Release: alt1.2.1

License: GPL v2+
Url: http://joey101.net/snowballz/
Group: Games/Arcade

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://joey101.net/snowballz/files/%name-%version.tar.bz2
Source1: %name.desktop
Patch: %name-util.py.patch

BuildArch: noarch

%description
Take command of your army of penguins as you blaze your path to
victory! March through snow laden forests to conquer new frontiers and
grow your small army. Ambush enemy lines with blasts of freezing
snowballs. But don't neglect your home, invaders are just over the
next snow drift! Gather fish for your cold penguins to munch on as
they warm up in your cozy igloo. It's a snowy world you don't want to
miss!

Snowballz is packed with adventure and fun yearning to be discovered.
Grab your free copy now and play by yourself or duel it out with your
friends. Well, what are you waiting for?

%prep
%setup -q
%patch

%install
install -d %buildroot{%_datadir/%name,%_bindir,%_desktopdir,%_pixmapsdir}

cat <<'EOF' >%buildroot%_bindir/%name
#!/bin/sh
cd %_datadir/%name
exec python snowballz.py $@
EOF

cp -fr buildings %buildroot%_datadir/%name
cp -fr data	 %buildroot%_datadir/%name
cp -fr gooeypy   %buildroot%_datadir/%name
cp -fr maps	 %buildroot%_datadir/%name
cp -fr plugins	 %buildroot%_datadir/%name
cp -f *.py	 %buildroot%_datadir/%name

install %SOURCE1 %buildroot%_desktopdir
# workaround for missing icon
install data/igloo.png %buildroot%_pixmapsdir/%name.png


%files
%doc AUTHORS README.txt
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5.1-alt1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5.1-alt1.2
- Rebuilt with python 2.6

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.9.5.1-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for snowballz

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 0.9.5.1-alt1.1
- Rebuilt with python-2.5.

* Tue Dec 25 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.5.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

