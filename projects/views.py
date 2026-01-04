from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def project_view(request, pk=None):

    if pk is None:

        if request.method == 'GET':
            projects = Project.objects.all()
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        project = get_object_or_404(Project, pk=pk)

        if request.method == 'GET':
            serializer = ProjectSerializer(project)
            return Response(serializer.data)

        elif request.method == 'PUT':
            if project.author != request.user:
                return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            serializer = ProjectSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if project.author != request.user:
                return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def contributor_view(request, pk=None):

    if pk is None:

        if request.method == 'GET':
            if 'project_id' in request.GET:
                id_du_projet = request.GET['project_id']
                contributors = Contributor.objects.filter(project=id_du_projet)
            else:
                contributors = Contributor.objects.all()

            serializer = ContributorSerializer(contributors, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ContributorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        contributor = get_object_or_404(Contributor, pk=pk)

        if request.method == 'GET':
            serializer = ContributorSerializer(contributor)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            contributor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def issue_view(request, pk=None):

    if pk is None:
        if request.method == 'GET':
            if 'project_id' in request.GET:
                id_du_projet = request.GET['project_id']
                issues = Issue.objects.filter(project=id_du_projet)
            else:
                issues = Issue.objects.all()

            serializer = IssueSerializer(issues, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = IssueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        issue = get_object_or_404(Issue, pk=pk)

        if request.method == 'GET':
            serializer = IssueSerializer(issue)
            return Response(serializer.data)

        elif request.method == 'PUT':
            if issue.author != request.user:
                 return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            serializer = IssueSerializer(issue, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if issue.author != request.user:
                 return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            issue.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def comment_view(request, pk=None):

    if pk is None:
        if request.method == 'GET':
            if 'issue_id' in request.GET:
                id_du_ticket = request.GET['issue_id']
                comments = Comment.objects.filter(issue=id_du_ticket)
            else:
                comments = Comment.objects.all()

            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        comment = get_object_or_404(Comment, pk=pk)

        if request.method == 'GET':
            serializer = CommentSerializer(comment)
            return Response(serializer.data)

        elif request.method == 'PUT':
            if comment.author != request.user:
                 return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            if comment.author != request.user:
                 return Response({"error": "Vous n'êtes pas l'auteur"}, status=status.HTTP_403_FORBIDDEN)

            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)