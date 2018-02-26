Name: jabber-jmc
Version: 0.3
Release: alt1.1.1

Summary: Jabber mail component
License: GPL
Group: System/Servers
Url: http://people.happycoders.org/dax/projects/jmc
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Source: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: jabber-common
BuildRequires: python-module-setuptools

Requires(pre): shadow-utils
Requires(post): %post_service jabber-common
Requires(preun): %preun_service

%description
JMC is a jabber service to check email from POP3 and IMAP4 server and retrieve them
or just a notification of new emails. Jabber users can register multiple email accounts.

%prep
%setup

%build
%__python setup.py build

%install
%__python setup.py install \
    --root=%buildroot \
    --optimize=2 \
    --record=INSTALLED_FILES

mkdir -p \
    %buildroot%_libdir/jmc \
    %buildroot%_logdir/jmc \
    %buildroot%_spooldir/jmc \
    %buildroot%_var/run/jmc

sed -i 's,@python_sitelibdir@,%python_sitelibdir,' jmc.init

install -pm0644 -D conf/jmc.conf %buildroot%_sysconfdir/jmc.conf
install -pm0755 -D jmc.init %buildroot%_initdir/jabber-jmc
install -pm0755 -D jmc.adapter %buildroot%_jabber_component_dir/jmc

# we have rpm for that, btw
sed -i -e '/egg-info/d' -e '/\/usr\/bin\/jmc/d' INSTALLED_FILES

%set_python_req_method strict

%pre
/usr/sbin/groupadd -r -f _jmc &>/dev/null
/usr/sbin/useradd -r -g _jmc -d /dev/null -s /dev/null \
    -c "Jabber mail component" -M -n _jmc &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files -f INSTALLED_FILES
%doc COPYING README TODO

%attr(0640,root,_jmc) %config(noreplace) %_sysconfdir/jmc.conf
%_initdir/%name
%_jabber_component_dir/jmc

%attr(0770,root,_jmc) %dir %_spooldir/jmc
%attr(0770,root,_jmc) %dir %_logdir/jmc
%attr(0770,root,_jmc) %dir %_var/run/jmc

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2008 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.1
- Rebuilt with python 2.6

* Sun Aug 31 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- Initial build for Sisyphus
