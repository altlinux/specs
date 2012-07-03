Name: chromeless
Version: 0.3
Release: alt3.1

Summary: A planform to create desktop applications using HTML and related Web technologies.
License: MPL 1.1/GPL 2.0+/LGPL 2.1+
Group: Development/Other
Url: http://github.com/mozilla/chromeless

Packager: Paul Wolneykien <manowar@altlinux.ru>
Source: %name-%version.tar

%define xulrunner %_libdir/xulrunner/xulrunner
%define xulrunner_pkg xulrunner
%define xulrunner_min 2.0.1

Requires: %name-tests = %version-%release
Requires: %name-examples = %version-%release
Requires: %name-doc-sources = %version-%release
Requires: %name-docs = %version-%release

BuildRequires: python >= 2.5
BuildConflicts: python > 3.0
BuildRequires: python-module-simplejson >= 1.9.2
BuildRequires: %xulrunner_pkg >= %xulrunner_min

%description
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

%package base
Summary: A planform to create desktop applications using HTML and related Web technologies.
Group: Development/Other
Requires: python >= 2.5
Conflicts: python > 3.0
Requires: python-module-simplejson >= 1.9.2
Requires: %xulrunner_pkg >= %xulrunner_min

%description base
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package contains the essential runtime and development files of the
platform.

%package tests
Summary: Unit-test files for the Chromeless platform.
Group: Development/Other
Requires: %name-base = %version-%release
BuildArch: noarch

%description tests
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package contains the unit-test files. To run the tests run
`chromless tests' command.

%package examples
Summary: Example applications for the Chromeless platform.
Group: Development/Other
Requires: %name-base = %version-%release
BuildArch: noarch

%description examples
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package contains the example applications that can be executed on
the platform. To run the tests run `chromless <path-to-example-dir>'
command. To run the default browser simply example run `chromeless'.

%package doc-sources
Summary: Documentation source files of the Chromeless platform.
Group: Development/Documentation
Requires: %name-base = %version-%release
BuildArch: noarch

%description doc-sources
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package contains the documentation source. To generate the static
documentation run `chromless docs' command. The resulting files are
written to the ~/.chromeless/build/docs. The prebuilt static
documentation can be found in the %name-docs package.

%package docs
Summary: Documentation files for the Chromeless platform.
Group: Development/Documentation
Requires: %name-base = %version-%release
BuildArch: noarch

%description docs
The 'chromeless' project is an experiment into making it possible to
build a web browser (or any other desktop application) using only web
technologies, like HTML, JavaScript, and CSS.

This package contains the prebuilt static documentation files.
In order to reproduce them the `chromless docs' command can be used.
The resulting files are written to the ~/.chromeless/build/docs.
The documentation source can be found in the %name-docs package.

%define cuddlefish_root %_libdir/chromeless
%define home_dir $HOME/.chromeless
%define tests_dir %_datadir/chromeless/tests
%define examples_dir %_datadir/chromeless/examples
%define docs_dir %_datadir/chromeless/docs

%prep
%setup

%build
# Link the xulrunner files
ln -s %xulrunner xulrunner
ln -s %xulrunner-bin xulrunner-bin

# Make the documentation
./chromeless docs

%install
# Install the main layout
mkdir -m0755 -p %buildroot%cuddlefish_root
cp -R --preserve=mode,timestamps {impl,modules} %buildroot%cuddlefish_root/
install -D -m0755 chromeless %buildroot%cuddlefish_root/chromeless
mkdir -m0755 -p %buildroot%tests_dir
cp -R --preserve=mode,timestamps tests/* %buildroot%tests_dir/
ln -s %tests_dir %buildroot%cuddlefish_root/tests
mkdir -m0755 -p %buildroot%examples_dir
cp -R --preserve=mode,timestamps examples/* %buildroot%examples_dir/
ln -s %examples_dir %buildroot%cuddlefish_root/examples
mkdir -m0755 -p %buildroot%docs_dir
cp -R --preserve=mode,timestamps docs/* %buildroot%docs_dir/
ln -s %docs_dir %buildroot%cuddlefish_root/docs

# Install the wrapper script
install -D -m0755 chromeless.sh %buildroot%_bindir/chromeless

# Install the xulrunner links and run-mozilla.sh script
install -D -m0755 run-mozilla.sh %buildroot%cuddlefish_root/run-mozilla.sh
ln -s %xulrunner %buildroot%cuddlefish_root/xulrunner
ln -s %xulrunner-bin %buildroot%cuddlefish_root/xulrunner-bin

# Configure the planform for system-wide usage
# Set the cuddlefish root directory path
sed -i -e 's|/usr/local/lib/chromeless|%cuddlefish_root|g' %buildroot%_bindir/chromeless

%files

%files base
%_bindir/*
%dir %cuddlefish_root
%cuddlefish_root/chromeless
%cuddlefish_root/xulrunner
%cuddlefish_root/xulrunner-bin
%cuddlefish_root/run-mozilla.sh
%cuddlefish_root/impl
%cuddlefish_root/modules
%dir %_datadir/chromeless
%dir %tests_dir
%cuddlefish_root/tests
%dir %examples_dir
%cuddlefish_root/examples
%dir %docs_dir
%cuddlefish_root/docs
%doc ChangeLog README.md

%files tests
%tests_dir/*

%files examples
%examples_dir/*

%files doc-sources
%docs_dir/*

%files docs
%doc %home_dir/build/docs/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt3.1
- Rebuild with Python-2.7

* Tue Aug 02 2011 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt3
- Require xulrunner instead of xulrunner-2.0.
- Shorten the package changelog (local modifications only).

* Wed Jul 13 2011 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt2
- Fix the extra separator after buildroot macros.

* Tue Jul 12 2011 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1
- Configure the xulrunner path relatively to the cuddlefish root.
- Search for the 'first browser' example from the cuddlefish root.
- Add the chromeless system-wide startup script.
- Write the test output to the home directory.
- Place the 'build' directory under the user home directory.
- Modify on-demand copies of application files.
- Require xulrunner v2.0.1 or higher.
- Add support for a default xulrunner configuration.
- Clone the Chromeless project from GitHub.
