%define pear_name HTML_Template_IT

Name: pear-HTML_Template_IT
Version: 1.2.1
Release: alt3

Summary: Integrated Templates

License: Modified BSD license
Group: Development/Other
Url: http://pear.php.net/package/HTML_Template_IT

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/HTML_Template_IT-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
HTML_Template_IT:
Simple template API.
The Isotemplate API is somewhat tricky for a beginner although it is the
best
one you can build. template::parse() [phplib template = Isotemplate]
requests
you to name a source and a target where the current block gets parsed
into.
Source and target can be block names or even handler names. This API gives
you
a maximum of fexibility but you always have to know what you do which is
quite unusual for php skripter like me.

I noticed that I do not any control on which block gets parsed into which
one.
If all blocks are within one file, the script knows how they are nested
and in
which way you have to parse them. IT knows that inner1 is a child of
block2, there's
no need to tell him about this.
Features :
  * Nested blocks
  * Include external file
  * Custom tags format (default {mytag})

HTML_Template_ITX :
With this class you get the full power of the phplib template class.
You may have one file with blocks in it but you have as well one main file
and multiple files one for each block. This is quite usefull when you have
user configurable websites. Using blocks not in the main template allows
you to modify some parts of your layout easily.

%prep
%setup -c

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
%pear_dir/HTML
%pear_testdir/HTML_Template_IT/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus

