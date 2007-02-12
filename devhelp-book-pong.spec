Summary:	DevHelp book: pong
Summary(pl.UTF-8):	Książka do DevHelpa o pongu
Name:		devhelp-book-pong
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/pong.tar.gz
# Source0-md5:	ecb7a53fb764d261fe79fe2f8e604e94
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/share/devhelp

%description
DevHelp book about pong.

%description -l pl.UTF-8
Książka do DevHelpa o pongu.

%prep
%setup -q -c -n pong

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/pong,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/pong.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/pong

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
