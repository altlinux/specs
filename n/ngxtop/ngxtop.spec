Name: ngxtop
Version: 0.0.2
Release: alt1

Summary:  Real-time metrics for nginx server

Url: https://github.com/lebinh/ngxtop
License: MIT
Group: Monitoring

Source: %name-%version.tar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires: python-module-distribute

%description
ngxtop parses your nginx access log and outputs useful,
top-like, metrics of your nginx server.
So you can tell what is happening with your server in real-time.

ngxtop is designed to run in a short-period time
just like the top command for troubleshooting
and monitoring your Nginx server at the moment.
If you need a long running monitoring process
or storing your webserver stats in external
monitoring / graphing system, you can try Luameter.

ngxtop tries to determine the correct location
and format of nginx access log file by default,
so you can just run ngxtop and having a close look
at all requests coming to your nginx server.
But it does not limit you to nginx and the default top view.
ngxtop is flexible enough for you to configure
and change most of its behaviours.
You can query for different things,
specify your log and format,
even parse remote Apache common access log with ease.
See sample usages below for some ideas about what you can do with it.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir/%{name}*.egg-info/

%changelog
* Sun Dec 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt1
- initial build for ALT Linux Sisyphus
