%define pear_name PHP_FunctionCallTracer

Name: pear-PHP_FunctionCallTracer
Version: 1.0.0
Release: alt3

Summary: Function Call Tracer

License: The BSD License
Group: Development/Other
Url: http://pear.php.net/package/PHP_FunctionCallTracer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/PHP_FunctionCallTracer-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
Creates a function calls debug trace. Functions arguments, returned
parameters and watched variables are reported in the same section for each
function call.
The trace is available as an array, or can be displayed or written in a
file.
Traced variables can be processed by provided user functions for
displaying purposes.

This package is not a replacement for full fledged PHP debuggers. It is
useful for (1) remote debugging, (2) to debug a complex sequence of
function calls, (3) to display non text variables in a user readable
format.

(1) Remote debugging is sometimes the only option to debug a package that
works fine on your system, e.g. a 32-bit OS, but breaks on a different
system, e.g. a 64-bit OS, which you have no access to. A remote user who
has the latter OS could run the package, then send you the trace for
analysis.

(2) It is sometimes difficult not to loose track of functions calls in
some live debugging sessions even with top notch PHP editor/debuggers. The
trace produced by this package may come handy and is easy to use in
combination with the source code to track calls and variables.

(3) Some variables native format does not always display well, typically:
packed data and UTF-8 strings. They can be converted as they are being
traced to a readable format by provided user functions. For example:
converting binary strings to hexadecimal, or UTF-8 string to Unicode.

Fully tested with phpUnit. Code coverage test close to 100%%.

Usage including trace examples is fully documented in docs/examples files.

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
%pear_testdir/PHP_FunctionCallTracer/
%pear_dir/PHP
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

