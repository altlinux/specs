%def_enable snapshot

%define _name Plots
%define pypi_name plots
%define ver_major 0.8
%define rdn_name com.github.alexhuntley.%_name

%def_disable check

Name: plots
Version: %ver_major.5
Release: alt1

Summary: A graph plotter for GNOME
License: GPL-3.0-or-later
Group: Education
Url: https://apps.gnome.org/Plots

%if_disabled snapshot
Source: https://github.com/alexhuntley/Plots/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/alexhuntley/Plots.git
Source: %name-%version.tar
%endif


Requires: typelib(Adw) = 1
Requires: font(dejavusans)
Requires: yelp
# rpm-build-python3 bug
Requires: python3(glm)
%filter_from_requires /python3(glm) < 0/d

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3(wheel) python3(setuptools)
BuildRequires: yelp-tools
BuildRequires: python3(OpenGL)
BuildRequires: python3(jinja2)
BuildRequires: python3(numpy)
BuildRequires: python3(lark)
BuildRequires: python3(PyGLM)
BuildRequires: python3(freetype)
#%{?_enable_check:BuildRequires: python3(pytest) python3(gi) typelib(Gtk) = 4.0}

%description
Plots is a graph plotting app for GNOME. Plots makes it easy to visualise
mathematical formulae. In addition to basic arithmetic operations, it supports
trigonometric, hyperbolic, exponential and logarithmic functions, as well as
arbitrary sums and products. It can display polar equations, and both implicit
and explicit Cartesian equations.

%prep
%setup %{?_disable_snapshot:-n %_name-%version}

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot/%_datadir/{applications,help,metainfo,locale}
cp res/%rdn_name.desktop %buildroot/%_datadir/applications/
cp res/%rdn_name.metainfo.xml %buildroot/%_datadir/metainfo

pushd help
for dir in $(ls); do
    mkdir -p %buildroot%_datadir/help/$dir/%name
    cp $dir/* %buildroot%_datadir/help/$dir/%name/; done
popd

mv %buildroot%python3_sitelibdir_noarch/%pypi_name/locale \
    -t %buildroot/%_datadir/
ln -s ../../../../share/locale \
    %buildroot%python3_sitelibdir_noarch/%pypi_name/locale

ln -sf ../../../../../share/fonts/ttf/dejavu/DejaVuSans.ttf \
    %buildroot%python3_sitelibdir_noarch/%pypi_name/res/DejaVuSans.ttf

%find_lang --with-gnome %name

%check
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3

%files -f %name.lang
%_bindir/%name
%python3_sitelibdir_noarch/%pypi_name/
%python3_sitelibdir_noarch/%_name-%version.dist-info
%_desktopdir/%rdn_name.desktop
#%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
#%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Nov 27 2023 Yuri N. Sedunov <aris@altlinux.org> 0.8.5-alt1
- first build for Sisyphus (v0.8.5-29-g39c1708)


