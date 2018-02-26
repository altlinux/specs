%define pear_name Games_Chess

Name: pear-Games_Chess
Version: 1.0.1
Release: alt2

Summary: Construct and validate a logical chess game, does not display

License: PHP License 3.01
Group: Development/Other
Url: http://pear.php.net/package/Games_Chess

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Games_Chess-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The logic of handling a chessboard and parsing standard
FEN (Forsyth-Edwards Notation) for describing a position as well as SAN
(Standard Algebraic Notation) for describing individual moves is handled.
This
class can be used as a backend driver for playing chess, or for validating
and/or creating PGN files using the File_ChessPGN package (when it is
completed).

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
%pear_dir/Games
%pear_testdir/Games_Chess/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus

