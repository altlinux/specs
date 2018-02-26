%define pear_name Image_Graph

Name: pear-Image_Graph
Version: 0.7.2
Release: alt3

Summary: Interface to AT&T's GraphViz tools

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/Image_Graph

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Image_Graph-%version.tgz

Patch1: Graph_Plot_Pie.patch
Patch2: checksum_correct.patch

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Image_Graph provides a set of classes that creates graphs/plots/charts
based on (numerical) data. Many different plot types are supported:
Bar, line, area, step, impulse, scatter, radar, pie, map, candlestick,
band, box &amp; whisker and smoothed line, area and radar plots.
The graph is highly customizable, making it possible to get the exact
look and feel that is required.
The output is controlled by a Image_Canvas, which facilitates easy
output to many different output formats, amongst others, GD (PNG,
JPEG, GIF, WBMP), PDF (using PDFLib), Scalable Vector Graphics (SVG).
Image_Graph is compatible with both PHP4 and PHP5.

%prep
%setup -c -n %pear_name-%version
%patch1 -p1
%patch2 -p1

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Image/
%pear_testdir/%pear_name/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Sun Jan 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt2
- add patch (http://www.maiamailguard.org/maia/ticket/326)

* Fri Jan 11 2008 Peter Evdokimov <peter@vpmes.ru> 0.7.2-alt1
- initial build for ALT Linux Sisyphus

