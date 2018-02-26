Name: arch-pqm
Version: 0.5
Release: alt1.1.1.1

Summary: arch patch queue manager
License: GPL
Group: Development/Other
Url: http://web.verbum.org/arch-pqm/
Packager: Alexey Voinov <voins@altlinux.ru>

BuildArch: noarch
Requires: python >= 2.3

Source: http://web.verbum.org/arch-pqm/download/%name-%version.tar.bz2
Source1: manual.html

# Automatically added by buildreq on Mon Oct 04 2004
BuildRequires: hostinfo python-base python-devel python-modules-encodings

%description 
The idea is simple. You have a project with a number of developers. With a
revision control system like CVS, it's obvious that the project code will be
kept in a single repository, which all the developers use. You really don't
have much of a choice.

But arch is fully distributed. You want to take advantage of those features,
allowing your developers to commit while disconnected (say while they are
travelling with a laptop), easily create their own temporary branches without
affecting the main repository, and more. To accomplish these things, each
developer needs to have their own arch archive.

This then raises a question - where is the project? One solution is to pick a
specific developer to perform the task of merging in the other developer's
code. That developer's archive becomes the canonical one for the project.

However, there is a better way. The main idea of the tla patch queue manager is
to have a special archive which is managed entirely by the patch queue
software.

%prep
%setup -q
cp %SOURCE1 ./

%build
%configure
make

%install
%makeinstall

%files
%doc manual.xml manual.html sample-arch-pqm.conf ChangeLog
%_bindir/*


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.5-alt1.1
- Rebuilt with python-2.5.

* Mon Oct 04 2004 Alexey Voinov <voins@altlinux.ru> 0.5-alt1
- initial build

