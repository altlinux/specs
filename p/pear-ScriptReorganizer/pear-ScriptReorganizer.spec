%define pear_name ScriptReorganizer

Name: pear-ScriptReorganizer
Version: 0.4.0
Release: alt1

Summary: Library/Tool focusing exclusively on the file size aspect of PHP script optimization

License: LGPL
Group: Development/Other
Url: http://pear.php.net/package/%pear_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/%pear_name-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildPreReq: pear-core rpm-build-pear

%description
ScriptReorganizer has the ability to reorganize source code in different
(incremental) ways:

- File: one-to-one (Script) or many-to-one (Library) optimization.

- Source: EOL (Route), comment (Quiet) and whitespace (Pack) optimization.

Plugin functionality is available by means of the Decorator Pattern.

It is highly recommended to follow the best practice detailed out below,
when using this package:

1. Running of all tests before building releases to deploy.

2. Reorganization of the source code file(s) with ScriptReorganizer.

3. Running of all tests - not only unit tests!

4. Final building of the release to deploy.

If the extreme mode of the pack strategy is used for packaging, a
non-ScriptReorganized source code tree should be shipped together with the
optimized one, to enable third parties to track down undiscoverd bugs.

Same applies for (complex) applications that are pharized, i.e. optimized
and packaged with PHP_Archive, as well as for bcompiled scripts.

ANN: Currently only pure PHP code can be reorganized. Look into the folder
root/PEAR/docs/ScriptReorganizer for more information in depth.

%prep
%setup -c
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/ScriptReorganizer/
%pear_testdir/ScriptReorganizer/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus (with pear make-rpm-spec)

