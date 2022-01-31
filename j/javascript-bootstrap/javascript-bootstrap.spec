%global _unpackaged_files_terminate_build 1

%define oname bootstrap
%global fontname glyphicons-halflings

Name: javascript-%oname
Summary: HTML, CSS and JS framework
Version: 3.4.1
Release: alt1
License: MIT
Group: Development/Other
Url: https://getbootstrap.com/
Source: %name-%version.tar
# Patch: %%name-%%version.patch
BuildArch: noarch
Provides: libjs-%oname = %EVR

Requires: javascript-common javascript-jquery fonts-glyphicons-halflings
BuildRequires(pre): rpm-macros-javascript rpm-macros-fontpackages

%description
Bootstrap is a popular HTML, CSS, and JS framework for developing
responsive, mobile first projects on the web.
It includes base CSS and HTML for typography, forms, buttons, tables,
grids, navigation, and more.


%package -n fonts-glyphicons-halflings
Summary: icons made for smaller graphic
Group: System/Fonts/True type
Conflicts: fonts-ttf-glyphicons-halflings

%description -n fonts-glyphicons-halflings
GLYPHICONS is a family of icon fonts
created with an emphasis to simplicity and easy orientation.
GLYPHICONS Halflings, a subset optimized for smaller graphics,
were freely licensed as part of Bootstrap 2.x and 3.x.

%prep
%setup
# %%patch -p1

%build
%install
mkdir -p %buildroot{%_jsdir/%oname/fonts,%_fontdir}
cp -p -r css %buildroot%_jsdir/%oname
cp -p -r js %buildroot%_jsdir/%oname
cp -p fonts/* %buildroot%_fontdir

for e in eot svg ttf woff woff2 ; do
    ln -r -s {%buildroot%_fontdir/glyphicons-halflings-regular,%buildroot%_jsdir/%oname/fonts/glyphicons-halflings-regular}.$e
done

%files
%_jsdir/%oname

%files -n fonts-glyphicons-halflings
%_fontdir

%changelog
* Tue Jan 25 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- Initial build.
