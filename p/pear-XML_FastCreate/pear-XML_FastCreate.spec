%define pear_name XML_FastCreate

Name: pear-XML_FastCreate
Version: 1.0.3
Release: alt4

Summary: Fast creation of valid XML with DTD control

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_FastCreate

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_FastCreate-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
- Easy way to make valid XML :
     $x->div(
         $x->h1("Example"),
         $x->p("Hello"),
         $x->p(array('class'=>'example'), "World !")
     )

- Option to report DTD errors in your XML :
  Use internal tool or external program [ Require XML_DTD package ]
- Use output driver of your choice :
  Text : return string
  XML_Tree : return XML_Tree object [ Require XML_Tree package ]
- Translate option to quickly transform tags by anothers :
   ex: Convert your XML to XHTML :
          <news><title> Example </title></news>
      =>  <div class="news"><h1><span> Example </span></h1></div>
- Include a PHP program to quickly transform HTML to FastCreate syntax.
  [ Require XML_HTMLSax package ]
- See examples for more informations :
  http://lya.fr/pear/XML_FastCreate/tests/
- French Tutorial :
  http://wiki.lya.fr/doku.php?id=pear_xml_fastcreate

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
%pear_dir/XML
%pear_dir/script
%pear_xmldir/%pear_name.xml

%changelog
* Wed Dec 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt4
- fix php requires

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- initial build for ALT Linux Sisyphus

