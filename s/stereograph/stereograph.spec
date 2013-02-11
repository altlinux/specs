Name: stereograph
Version: 0.30a
Release: alt2

Summary: Stereogram generator

License: GPL
Group: Graphics
Url: http://januszewski.de/stereogramm-howto-de.html

Packager: Dmitry Derjavin <dd@altlinux.org>

Source: %name-%version.tar
Patch1: stereograph-0.30a-alt-libpng-1.5.x.patch

BuildRequires: zlib-devel libpng-devel

%description
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That is a program that produces
two-dimensional images that seem to be three-dimensional (surely you
know the famous works of "The Magic Eye", Stereograph produces the
same output). You do _not_ need any pair of colored spectacles to
regard them - everyone can learn it.

%prep
%setup -q

%patch1 -p0

%build
for module in stereograph renderer gfxio; do
    gcc -O2 -Dlinux -c -o $module.o $module.c
done
gcc stereograph.o renderer.o gfxio.o -o stereograph -lm -lz -lpng

%install
install -pD -m 755 %name %buildroot%_bindir/%name
install -pD -m 644 %name\.1 %buildroot%_man1dir/%name\.1

%files
%_bindir/%name
%_man1dir/*
%doc README ChangeLog AUTHORS

%changelog
* Mon Feb 11 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt2
- Fix to build against libpng-1.5.x.

* Sat Feb 09 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt1
- Build for Sisyphus.

* Fri Feb 08 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt0.M60P.1
- Initial build for ALT Linux P6.

