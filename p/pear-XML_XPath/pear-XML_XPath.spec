%define pear_name XML_XPath

Name: pear-XML_XPath
Version: 1.2.4
Release: alt3

Summary: The PEAR::XML_XPath class provided an XPath/DOM XML manipulation, maneuvering and query interface

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_XPath

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_XPath-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The PEAR::XML_XPath class provided an XPath/DOM XML manipulation,
maneuvering and query interface.  The class allows for easy manipulation,
maneuvering and querying of a domxml tree using both xpath queries
and DOM walk functions.  It uses an internal pointer for all methods
on which the action is performed.  Results from an dom/xpath query are
returned as an XPath_Result object, which contains an internal array of
DOM nodes and which extends the common DOM class and hence contains all
the DOM functions from the main object to run on each of the elements
in the internal array.  This class tries to hold as close as possible
to the DOM Recommendation.  You MUST have the domxml extension to use
this class.  The XML_XPath class was inspired by a class maintained
by Nigel Swinson called phpxpath.  The phpxpath class does not rely
on PHP xmldom functions and is therefore a sibling to this class:
http://sourceforge.net/projects/phpxpath

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
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.4-alt1
- initial build for ALT Linux Sisyphus

