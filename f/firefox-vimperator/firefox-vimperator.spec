%define vname	vimperator
%define mname	muttator
%define vcid vimperator@mozdev.org
%define mcid muttator@mozdev.org
%define vciddir 	%firefox_noarch_extensionsdir/%vcid
%define mciddir 	%tbird_noarch_extensionsdir/%mcid
%define ver 3.4
%define mver 1.1
%define ft_release alt1.hg20120115
%define workdir %firefox_name-%vname-%ver
%define mworkdir %tbird_name-%mname-%mver

Name: %firefox_name-%vname
Version: %ver
Release: %ft_release
Summary: Browser add-on for Firefox, which makes it like the Vim text editor
Group: Networking/WWW
License: MPL 1.1/GPL 2.0/LGPL 2.1
URL: http://%vname.org/
# hg clone https://code.google.com/p/vimperator-labs/
Source: %firefox_name-%vname-%version.tar.bz2
Source1: asciidoc.tar.bz2
Requires: %firefox_name >= 3.0
Requires: vim
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch
BuildRequires(pre): rpm-build-firefox rpm-build-thunderbird rpm-build-vim
BuildRequires(pre): java-devel-default
BuildPreReq: zip python-modules

%description 
Vimperator is a free browser add-on for Firefox, which makes it look and behave
like the Vim text editor. It has similar key bindings and you could call it a
modal web browser, as key bindings differ according to which mode you are in.

Warning: To provide the most authentic Vim experience, Vimperator hides the
Firefox menubar and toolbar by default. Most users find them unnecessary once
they're used to Vimperator, but if you really need them, type: :set
guioptions+=mT to get them back.

If you don't like Vimperator at all, you can uninstall it by typing :addons and
removing/disabling it. If you like it, but can't remember the shortcuts, press
F1 or :help.

%package -n %tbird_name-%mname
Summary: Add-on for Thunderbird, which makes Thunderbird behave like Vim
Version: %mver
Release: %ft_release
Group: Networking/Mail
BuildArch: noarch
Requires: %tbird_name >= %tbird_version

%description -n %tbird_name-%mname
Muttator is a free browser add-on for Thunderbird, which makes it look and
behave like the Vim text editor. It has similar key bindings, and you could call
it a modal mail client, as key bindings differ according to which mode you are
in.

Warning: To provide the most authentic Vim experience, the Thunderbird menubar
and toolbar were hidden.

If you really need them, type: [set guioptions+=mT to get them back.
If you don't like Muttator at all, you can uninstall it by typing
:addons and remove/disable it.
If you like it, but can't remember the shortcuts, press F1 or :help to get this
help window back.

%prep
%setup
tar -xjf %SOURCE1

%build
ln -s asciidoc.py asciidoc/asciidoc
export PATH=$PWD/asciidoc:$PATH
%make_build

mkdir -p _%vname
cp %vname/%{vname}rc.example _%vname/
pushd _%vname
%jar xf ../downloads/%{vname}*.xpi
popd

mkdir -p _%mname
pushd _%mname
%jar xf ../downloads/%{mname}*.xpi
popd

%install
install -d %buildroot%vciddir
install -d %buildroot%mciddir
install -d %buildroot%vim_syntax_dir
install -d %buildroot%vim_ftdetect_dir
cp -fR _%vname/* %buildroot%vciddir/
cp -fR _%mname/* %buildroot%mciddir/
install -m644 %vname/contrib/vim/syntax/%vname.vim \
	%buildroot%vim_syntax_dir/
install -m644 %mname/contrib/vim/syntax/%mname.vim \
	%buildroot%vim_syntax_dir/
install -m644 %vname/contrib/vim/ftdetect/%vname.vim \
	%buildroot%vim_ftdetect_dir/
install -m644 %mname/contrib/vim/ftdetect/%mname.vim\
	%buildroot%vim_ftdetect_dir/

%files
%vciddir
%vim_syntax_dir/%vname.vim
%vim_ftdetect_dir/%vname.vim

%files -n %tbird_name-%mname
%mciddir
%vim_syntax_dir/%mname.vim
%vim_ftdetect_dir/%mname.vim

%changelog
* Thu Jan 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.hg20120115
- Version 3.4

* Thu Aug 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.hg20110728
- Version 3.3

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0pre-alt1.hg20101113
- Version 3.0pre

* Thu Aug 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4pre-alt1.hg20100810
- Version 2.4pre

* Tue Feb 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3a1pre-alt1.hg20100214
- Version 2.3a1pre

* Fri Oct 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.b1-alt1.hg20091022
- Version 2.2.b1

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt3.git20090727
- Rebuild with asciidoc 8.2.7 (ALT #20851)

* Thu Jul 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20090723
- Updated from upstream git repository
- Resolved (ALT #20851)

* Tue Apr 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20090428
- New version
- Add Muttator add-on for Thunderbird
- Rebuild with new libtool

* Thu Mar 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0pre-alt1.git20090319
- New trunk from upstream
- Build with dependency of Firefox >= 3.1

* Fri Jan 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0pre-alt1.git20090109
- Initial build for Sisyphus
